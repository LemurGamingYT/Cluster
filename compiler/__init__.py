from dataclasses import dataclass
from sys import exit as sys_exit
from typing import NoReturn
from pathlib import Path

from antlr4 import Token, CommonTokenStream, FileStream
from antlr4.tree.Tree import TerminalNodeImpl

from compiler.cpp_info import (
    reserved, parse_cpp_file, DEFAULT_HEADER, lang_type_to_cpp, cpp_type_to_lang, is_cpp_type
)
from compiler.parser.ClusterVisitor import ClusterVisitor
from compiler.error_listener import ClusterErrorListener
from compiler.parser.ClusterParser import ClusterParser
from compiler.parser.ClusterLexer import ClusterLexer
from compiler.file_validator import validate_file
from compiler.std import LIBRARIES


op_symbol_to_name_map = {
    '+': 'add',
    '-': 'sub',
    '*': 'mul',
    '/': 'div_',
    '%': 'mod',
    '==': 'eq',
    '!=': 'neq',
    '>': 'gt',
    '<': 'lt',
    '>=': 'gte',
    '<=': 'lte',
    '&&': 'and_',
    '||': 'or_',
    '!': 'not_',
}


@dataclass(slots=True, unsafe_hash=True, eq=False)
class Statement:
    code: str
    type: str
    position: tuple[int, int]


def to_position(ctx) -> tuple[int, int]:
    if isinstance(ctx, TerminalNodeImpl):
        ctx = ctx.getSymbol()
        return (ctx.line, ctx.column)
    elif isinstance(ctx, Token):
        return (ctx.line, ctx.column)

    return (ctx.start.line, ctx.start.column)


def _print(_, args: list[Statement], call_position: tuple[int, int]) -> Statement:
    if len(args) < 1:
        return Statement(f'print("")', 'nil', call_position)

    arg1 = args[0]
    if arg1.type == 'string':
        arg1 = arg1.code
    else:
        arg1 = f'repr({arg1.code})'

    return Statement(f'print({arg1})', 'nil', call_position)

def _type(compiler, args: list[Statement], call_position: tuple[int, int]) -> Statement:
    if len(args) < 1:
        compiler.err('Type', 'Not enough arguments', call_position)

    arg1 = args[0]
    return Statement(f'type({arg1.code})', 'string', call_position)

def _to_string(compiler, args: list[Statement], call_position: tuple[int, int]) -> Statement:
    if len(args) < 1:
        compiler.err('Type', 'Not enough arguments', call_position)

    arg1 = args[0]
    return Statement(f'repr({arg1.code})', 'string', call_position)

def _input(_, args: list[Statement], call_position: tuple[int, int]) -> Statement:
    prompt = '(string_t) ""'
    if len(args) > 0:
        prompt = args[0].code
    
    return Statement(f'input({prompt})', 'string', call_position)


DEFAULT_ENV = {
    'print': ('nil', _print),
    'type': ('string', _type),
    'to_string': ('string', _to_string),
    'input': ('string', _input),
    'range': 'arrayType<int_t>'
}


def err(error_type: str, error_message: str, position: tuple[int, int], src: str) -> NoReturn:
    print(src.splitlines()[position[0]-1])
    print(f'{" " * position[1]}^')
    print(f'{error_type}Error: {error_message}')
    sys_exit(1)


def make_env() -> dict:
    _, _, _, types = parse_cpp_file(DEFAULT_HEADER)
    return DEFAULT_ENV.copy() | {t: t for t in types}


class ClusterCompiler(ClusterVisitor):
    def __init__(self, file: Path) -> None:
        self.operations, self.attributes, _, _ = parse_cpp_file(DEFAULT_HEADER)
        self.top_scope_code = ''
        self.env = make_env()
        self.env['FILE'] = 'string'

        self.src = file.read_text()
    
    
    def compile(self, file: Path, extension: str = '.cpp') -> Path:
        fstream = FileStream(file.as_posix(), 'utf-8')

        lexer = ClusterLexer(fstream)
        tokens = CommonTokenStream(lexer)

        parser = ClusterParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(ClusterErrorListener(self.src, self.err))
        tree = parser.parse()

        compiler = ClusterCompiler(file)
        code = compiler.visitParse(tree)

        src = ''
        for stmt in code:
            src += stmt.code + '\n'

        cpp = file.with_suffix(extension)
        include_header = f'#include "{DEFAULT_HEADER.absolute().as_posix()}"'
        file_name = f'#define FILE "{file.absolute().as_posix()}"'
        cpp.write_text(
            validate_file(
                f'{include_header}\n{compiler.top_scope_code}\n\n{file_name}\n\n{src}\n',
                compiler.err
            )
        )

        return cpp

    def err(self, error_type: str, error_message: str, position: tuple[int, int]) -> NoReturn:
        err(error_type, error_message, position, self.src)


    def get_name(self, identifier: str, position: tuple[int, int]) -> str:
        if identifier not in self.env:
            self.err('Name', f'Unknown identifier \'{identifier}\'', position)

        return self.env[identifier]
    
    def validate_name(self, name: str, position: tuple[int, int]) -> bool:
        if name in reserved:
            self.err('Name', f'Reserved name \'{name}\' cannot be used as a name', position)
        
        return True

    def condition(self, expr: ClusterParser.ExprContext) -> Statement:
        ctx = expr
        expr = self.visitExpr(expr)
        if expr.type != 'bool':
            expr = f'tobool({expr.code})'
        else:
            expr = expr.code

        return Statement(expr, 'bool', to_position(ctx))


    def visitParse(self, ctx: ClusterParser.ParseContext) -> list[Statement]:
        return [self.visitStmt(stmt) for stmt in ctx.stmt()]
    
    def visitType(self, ctx: ClusterParser.TypeContext) -> str:
        if ctx.LBRACK() is not None and ctx.ID(0).getText() == 'array':
            return f'arrayType<{lang_type_to_cpp(ctx.ID(1).getText())}>'
        elif ctx.LBRACK() is not None and ctx.ID(0).getText() != 'array':
            self.err('Type', 'Invalid array type', to_position(ctx))

        return lang_type_to_cpp(ctx.getText())

    def visitArg(self, ctx: ClusterParser.ArgContext) -> Statement:
        return self.visitExpr(ctx.expr())

    def visitArgs(self, ctx: ClusterParser.ArgsContext) -> list[Statement]:
        return [self.visitArg(arg) for arg in ctx.arg()] if ctx is not None else []

    def visitParam(self, ctx: ClusterParser.ParamContext) -> Statement:
        return Statement(
            f'{self.visitType(ctx.type_())} {ctx.ID().getText()}',
            'nil',
            to_position(ctx)
        )

    def visitParams(self, ctx: ClusterParser.ParamsContext) -> list[Statement]:
        return [self.visitParam(param) for param in ctx.param()] if ctx is not None else []
    
    def visitIfStmt(self, ctx: ClusterParser.IfStmtContext) -> Statement:
        condition = self.condition(ctx.expr())
        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        else_body = '' if ctx.elseStmt() is None else self.visitElseStmt(ctx.elseStmt()).code
        elseifs = ' '.join(self.visitElseIfStmt(elseif).code for elseif in ctx.elseifStmt())
        return Statement(
            f'if ({condition.code}) {{\n{body}\n}}{elseifs}{else_body}',
            'nil',
            to_position(ctx)
        )
    
    def visitElseStmt(self, ctx: ClusterParser.ElseStmtContext) -> Statement:
        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        return Statement(f' else {{\n{body}\n}}', 'nil', to_position(ctx))
    
    def visitElseIfStmt(self, ctx: ClusterParser.ElseifStmtContext) -> Statement:
        condition = self.condition(ctx.expr())
        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        return Statement(f' else if ({condition.code}) {{\n{body}\n}}', 'nil', to_position(ctx))
    
    def visitWhileStmt(self, ctx: ClusterParser.WhileStmtContext) -> Statement:
        condition = self.condition(ctx.expr())
        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        return Statement(f'while ({condition.code}) {{\n{body}\n}}', 'nil', to_position(ctx))
    
    def visitUseStmt(self, ctx: ClusterParser.UseStmtContext) -> Statement:
        lib_names = [s.getText()[1:-1] for s in ctx.STRING()]
        for lib in lib_names:
            header = LIBRARIES.get(lib)
            if header is None:
                self.err('Import', f'Unknown library \'{lib}\'', to_position(ctx))

            lib_ops, lib_attrs, lib_funcs, lib_types = parse_cpp_file(Path(header))
            self.operations.update(lib_ops)
            self.attributes.update(lib_attrs)
            self.env.update(lib_funcs | {t: t for t in lib_types})
            self.top_scope_code += f'#include "{header}"\n'

        return Statement(f'// using {", ".join(lib_names)}', 'nil', to_position(ctx))

    def visitBodyStmts(self, ctx: ClusterParser.BodyStmtsContext) -> Statement:
        if ctx.RETURN() is not None:
            expr = self.visitExpr(ctx.expr())
            return Statement(f'return {expr.code}', expr.type, to_position(ctx.RETURN()))
        elif ctx.stmt() is not None:
            return self.visitStmt(ctx.stmt())

    def visitBody(self, ctx: ClusterParser.BodyContext) -> list[Statement]:
        return [self.visitBodyStmts(stmt) for stmt in ctx.bodyStmts()]
    
    def visitVarAssign(self, ctx: ClusterParser.VarAssignContext) -> Statement:
        name = ctx.ID().getText()
        value = self.visitExpr(ctx.expr())
        if name in self.env:
            return Statement(f'{name} = {value.code}', value.type, to_position(ctx.ID()))

        typ = lang_type_to_cpp(value.type)
        self.env[name] = value.type
        return Statement(f'{typ} {name} = {value.code}', value.type, to_position(ctx.ID()))

    def visitFuncAssign(self, ctx: ClusterParser.FuncAssignContext) -> Statement:
        self.validate_name(ctx.ID().getText(), to_position(ctx.ID()))
        name = ctx.ID().getText()
        params = self.visitParams(ctx.params())
        ret_type = self.visitType(ctx.type_()) if ctx.type_() is not None else 'nil'
        self.env[name] = ret_type
        current_env = self.env.copy()
        self.env = self.env.copy()
        for param in params:
            self.env[param.code.split()[1]] = param.code.split()[0]

        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        self.env = current_env

        return Statement(
            f"""{lang_type_to_cpp(ret_type)} {name}({", ".join(param.code for param in params)}) {{
{body}{"\nreturn nil_t()" if ret_type == "nil" else ""}
}}\n""",
            'nil', to_position(ctx.ID())
        )
    
    def visitAtom(self, ctx: ClusterParser.AtomContext) -> Statement:
        if ctx.INT() is not None:
            return Statement(f'(int_t){ctx.getText()}', 'int', to_position(ctx))
        elif ctx.FLOAT() is not None:
            return Statement(f'(float_t){ctx.getText()}', 'float', to_position(ctx))
        elif ctx.STRING() is not None:
            return Statement(f'(string_t)"{ctx.getText()[1:-1]}"', 'string', to_position(ctx))
        elif ctx.BOOL() is not None:
            return Statement(f'{ctx.getText()}', 'bool', to_position(ctx))
        elif ctx.ID() is not None:
            return Statement(
                ctx.getText(),
                self.get_name(ctx.getText(), to_position(ctx)),
                to_position(ctx)
            )
        elif ctx.NIL() is not None:
            return Statement(f'nullptr', 'nil', to_position(ctx))
        elif ctx.HEX() is not None:
            return Statement(f'(hex_t) {ctx.getText()}', 'hex', to_position(ctx))
        elif ctx.expr() is not None:
            return self.visitExpr(ctx.expr())
        elif ctx.LBRACE() is not None:
            array_type = self.visitType(ctx.type_())
            args = self.visitArgs(ctx.args())
            return Statement(
                f'new_array<{array_type}>({{{", ".join(arg.code for arg in args)}}})',
                f'arrayType<{array_type}>',
                to_position(ctx)
            )
    
    def visitCall(self, ctx: ClusterParser.CallContext) -> Statement:
        env_item = self.get_name(ctx.ID().getText(), to_position(ctx.ID()))
        args = self.visitArgs(ctx.args())
        if isinstance(env_item, tuple):
            returns = env_item[0]
            func = env_item[1]
            return func(self, args, to_position(ctx.ID()))
        else:
            returns = env_item

        return Statement(
            f'{ctx.ID().getText()}({", ".join(arg.code for arg in args)})',
            returns,
            to_position(ctx.ID())
        )
    
    def visitExpr(self, ctx: ClusterParser.ExprContext) -> Statement:
        if ctx.atom() is not None:
            return self.visitAtom(ctx.atom())
        elif ctx.call() is not None:
            return self.visitCall(ctx.call())
        elif ctx.NOT() is not None:
            left = self.visitExpr(ctx.expr(0))
            op = self.operations[op_symbol_to_name_map[ctx.NOT().getText()]]
            operation = op.get((lang_type_to_cpp(left.type),))
            if operation is None:
                self.err(
                    'Type',
                    f'Invalid operation \'!\' on type \'{left.type}\'',
                    to_position(ctx.NOT())
                )

            return Statement(
                f'{op_symbol_to_name_map[ctx.NOT().getText()]}({left.code})',
                operation,
                to_position(ctx.NOT())
            )
        elif ctx.op is not None:
            left = self.visitExpr(ctx.expr(0))
            right = self.visitExpr(ctx.expr(1))
            op = ctx.op.text

            op_name = op_symbol_to_name_map[op]
            operation = self.operations[op_name].get((
                lang_type_to_cpp(left.type), lang_type_to_cpp(right.type)
            ))
            if operation is None:
                self.err(
                    'Type',
                    f'Invalid operation \'{op}\' between types \'{left.type}\' and \'{right.type}\'',
                    to_position(ctx.op)
                )

            return Statement(
                f'{op_name}({left.code}, {right.code})',
                operation,
                to_position(ctx.op)
            )
        elif ctx.DOT() is not None:
            attr_name = ctx.ID().getText()
            obj = self.visitExpr(ctx.expr(0))
            obj_type = obj.type
            if obj_type.startswith('arrayType<'):
                obj_type = 'array'
            elif is_cpp_type(obj_type):
                obj_type = cpp_type_to_lang(obj_type)

            if obj_type not in self.attributes:
                self.err(
                    'Type',
                    f'Invalid attribute \'{attr_name}\' for type \'{obj_type}\'',
                    to_position(ctx)
                )

            if attr_name not in self.attributes[obj_type]:
                self.err(
                    'Attribute',
                    f'Invalid attribute \'{attr_name}\' for type \'{obj_type}\'',
                    to_position(ctx)
                )
            
            attribute = self.attributes[obj_type][attr_name]
            if attribute['method'] and ctx.LPAREN() is None:
                self.err(
                    'Attribute',
                    f'Attribute \'{attr_name}\' is a method and needs to be called',
                    to_position(ctx)
                )

            args = []
            if not attribute['static']:
                args.append(obj)

            if ctx.LPAREN() is not None and attribute['method']:
                args.extend(self.visitArgs(ctx.args()))
                return Statement(
                    f'{obj_type}_{attr_name}({", ".join(arg.code for arg in args)})',
                    attribute['ret'],
                    to_position(ctx)
                )
            elif attribute['property']:
                return Statement(
                    f'{obj_type}_{attr_name}({", ".join(arg.code for arg in args)})',
                    attribute['ret'],
                    to_position(ctx)
                )
            else:
                self.err(
                    'Attribute',
                    f'Invalid attribute invoke \'{attr_name}\' for type \'{obj_type}\'',
                    to_position(ctx)
                )
