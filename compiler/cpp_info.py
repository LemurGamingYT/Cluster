from dataclasses import dataclass, field
from pathlib import Path


DEFAULT_HEADER = Path(__file__).parent / 'cluster.hpp'

ops = {
    'add', 'sub', 'mul', 'div_', 'mod', 'eq', 'neq', 'gt', 'lt', 'gte', 'lte', 'and_', 'or_', 'not_'
}

reserved = {
    'type', 'int_t', 'float_t', 'string_t', 'bool_t', 'nil_t', 'Math', 'repr', 'tobool', 'print',
    'MathType'
} | ops

lang_type_map = {
    'int': 'int_t',
    'float': 'float_t',
    'string': 'string_t',
    'bool': 'bool_t',
    'nil': 'nil_t',
    'array': 'arrayType',
}


@dataclass(slots=True, unsafe_hash=True)
class Param:
    type: str = field(default='')
    name: str = field(default='_')


@dataclass(slots=True, unsafe_hash=True)
class CppInfo:
    header: Path = field(default=DEFAULT_HEADER)
    operations: dict = field(default_factory=dict)
    attributes: dict = field(default_factory=dict)
    functions: dict = field(default_factory=dict)
    types: list = field(default_factory=list)
    
    def __iter__(self):
        return iter((self.operations, self.attributes, self.functions, self.types))


@dataclass(slots=True, unsafe_hash=True)
class Attribute:
    ret: str
    static: bool
    method: bool
    property: bool
    func: bool

    def __getitem__(self, key: str):
        return getattr(self, key)


def get_function_name(line: str) -> str:
    return line.split()[2].split('(')[0].removesuffix(')')

def get_function_type(line: str) -> str:
    return line.split()[1]

def get_function_parameters(line: str) -> list[Param]:
    params = line.split('(')[1].split(')')[0].split(',')
    return [Param(*param.split()) for param in params]


def lang_type_to_cpp(type: str) -> str:
    return lang_type_map.get(type, type)

def cpp_type_to_lang(type: str) -> str:
    return list(lang_type_map.keys())[list(lang_type_map.values()).index(type)]

def is_cpp_type(type: str) -> bool:
    return type in lang_type_map.values()

def is_lang_type(type: str) -> bool:
    return type in lang_type_map


def parse_cpp_file(file_path: Path) -> tuple[dict]:
    info = CppInfo(file_path)
    
    content = file_path.read_text().splitlines()
    i = 0
    while i < len(content):
        line = content[i]
        if line.startswith('// types: '):
            info.types.extend(line.removeprefix('// types: ').split(', '))
        elif line.startswith('inline '):
            name = get_function_name(line)
            ret_type = get_function_type(line)
            params = get_function_parameters(line)
            if name in ops:
                info.operations.setdefault(name, {})
                info.operations[name][tuple(param.type for param in params)] = ret_type
            else:
                comments = {'static': False, 'method': False, 'property': False, 'func': False}
                if i - 1 >= 0:
                    if content[i-1].startswith('// '):
                        content[i-1] = content[i-1].removeprefix('// ')
                        for comment in content[i-1].split():
                            comments[comment] = True

                if comments['func']:
                    info.functions[name] = ret_type
                elif '_' in name:
                    attr_for, attr_name = name.split('_', 1)
                    info.attributes.setdefault(attr_for, {})

                    info.attributes[attr_for][attr_name] = Attribute(ret_type, **comments)

        i += 1

    return info
