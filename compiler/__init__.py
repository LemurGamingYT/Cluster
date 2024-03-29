from dataclasses import dataclass
from sys import exit as sys_exit
from typing import NoReturn

from antlr4.tree.Tree import TerminalNodeImpl
from antlr4 import Token

from compiler.cpp_info import reserved, lang_type_map, parse_cpp_file, DEFAULT_HEADER
from compiler.parser.ClusterVisitor import ClusterVisitor
from compiler.parser.ClusterParser import ClusterParser


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


DEFAULT_ENV = {
    'print': ('nil', _print),
    'type': ('string', _type),
    'to_string': ('string', _to_string),
    'Math': 'Math'
}


class ClusterCompiler(ClusterVisitor):
    def __init__(self, src: str) -> None:
        self.operations, self.attributes = parse_cpp_file(DEFAULT_HEADER)
        self.env = DEFAULT_ENV

        self.src = src


    def err(self, error_type: str, error_message: str, position: tuple[int, int]) -> NoReturn:
        print(self.src.splitlines()[position[0]-1])
        print(f'{" " * position[1]}^')
        print(f'{error_type}Error: {error_message}')
        sys_exit(1)

    def get_name(self, identifier: str, position: tuple[int, int]) -> str:
        if identifier not in self.env:
            self.err('Name', f'Unknown identifier \'{identifier}\'', position)

        return self.env[identifier]
    
    def validate_name(self, name: str, position: tuple[int, int]) -> bool:
        if name in reserved:
            self.err('Name', f'Reserved name \'{name}\' cannot be used as a function name', position)
        
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
        return lang_type_map.get(ctx.getText(), ctx.getText())

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
        return Statement(f'if ({condition.code}) {{\n{body}\n}}', 'nil', to_position(ctx))
    
    def visitWhileStmt(self, ctx: ClusterParser.WhileStmtContext) -> Statement:
        condition = self.condition(ctx.expr())
        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        return Statement(f'while ({condition.code}) {{\n{body}\n}}', 'nil', to_position(ctx))

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

        self.env[name] = value.type
        return Statement(f'{value.type} {name} = {value.code}', value.type, to_position(ctx.ID()))

    def visitFuncAssign(self, ctx: ClusterParser.FuncAssignContext) -> Statement:
        self.validate_name(ctx.ID().getText(), to_position(ctx.ID()))
        name = ctx.ID().getText()
        params = self.visitParams(ctx.params())
        ret_type = self.visitType(ctx.type_()) if ctx.type_() is not None else 'nil'
        self.env[name] = ret_type
        current_env = self.env.copy()
        self.env = DEFAULT_ENV
        for param in params:
            self.env[param.code.split()[1]] = param.code.split()[0]

        body = '\n'.join(stmt.code for stmt in self.visitBody(ctx.body()))
        self.env = current_env

        self.env[name] = ret_type
        return Statement(
            f"""{ret_type} {name}({", ".join(param.code for param in params)}) {{
{body}{"\nreturn nil_t()" if ret_type == "nil" else ""}
}}\n""",
            'nil', to_position(ctx.type_())
        )
    
    def visitAtom(self, ctx: ClusterParser.AtomContext) -> Statement:
        if ctx.INT() is not None:
            return Statement(f'(int_t){ctx.getText()}', 'int', to_position(ctx))
        elif ctx.FLOAT() is not None:
            return Statement(f'(float_t){ctx.getText()}', 'float', to_position(ctx))
        elif ctx.STRING() is not None:
            return Statement(f'(string_t){ctx.getText()}', 'string', to_position(ctx))
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
        elif ctx.expr() is not None:
            return self.visitExpr(ctx.expr())
    
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
        elif ctx.op is not None:
            left = self.visitExpr(ctx.expr(0))
            right = self.visitExpr(ctx.expr(1))
            op = ctx.op.text
            
            if right.code == '0' and op == '/':
                self.err(
                    'Type',
                    'Division by zero',
                    to_position(ctx)
                )

            op_name = op_symbol_to_name_map[op]
            operation = self.operations[op_name].get((
                lang_type_map.get(left.type, left.type), lang_type_map.get(right.type, right.type)
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

            if obj.type not in self.attributes:
                self.err(
                    'Type',
                    f'Invalid attribute \'{attr_name}\' for type \'{obj.type}\'',
                    to_position(ctx)
                )

            if attr_name not in self.attributes[obj.type]:
                self.err(
                    'Attribute',
                    f'Invalid attribute \'{attr_name}\' for type \'{obj.type}\'',
                    to_position(ctx)
                )
            
            attribute = self.attributes[obj.type][attr_name]
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
                    f'{obj.type}_{attr_name}({", ".join(arg.code for arg in args)})',
                    attribute['ret'],
                    to_position(ctx)
                )
            elif attribute['property']:
                return Statement(
                    f'{obj.type}_{attr_name}({", ".join(arg.code for arg in args)})',
                    attribute['ret'],
                    to_position(ctx)
                )
            else:
                self.err(
                    'Attribute',
                    f'Invalid attribute invoke \'{attr_name}\' for type \'{obj.type}\'',
                    to_position(ctx)
                )
