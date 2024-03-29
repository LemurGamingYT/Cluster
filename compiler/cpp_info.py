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
    'Math': 'Math'
}


@dataclass(slots=True, unsafe_hash=True)
class Param:
    type: str = field(default='')
    name: str = field(default='_')


@dataclass(slots=True, unsafe_hash=True)
class Attribute:
    ret: str
    static: bool
    method: bool
    property: bool

    def __getitem__(self, key: str):
        return getattr(self, key)


def get_function_name(line: str) -> str:
    return line.split()[2].split('(')[0].removesuffix(')')

def get_function_type(line: str) -> str:
    return line.split()[1]

def get_function_parameters(line: str) -> list[Param]:
    params = line.split('(')[1].split(')')[0].split(',')
    return [Param(*param.split()) for param in params]


def parse_cpp_file(file_path: Path) -> tuple[dict]:
    operations, attributes = {}, {}
    
    content = file_path.read_text().splitlines()
    i = 0
    while i < len(content):
        line = content[i]
        if line.startswith('inline '):
            name = get_function_name(line)
            ret_type = get_function_type(line)
            params = get_function_parameters(line)
            if name in ops:
                operations.setdefault(name, {})
                operations[name][tuple(param.type for param in params)] = ret_type
            else:
                if '_' in name:
                    attr_for, attr_name = name.split('_', 1)
                    attributes.setdefault(attr_for, {})

                    comments = {'static': False, 'method': False, 'property': False}
                    if content[i-1].startswith('// '):
                        content[i-1] = content[i-1].removeprefix('// ')
                        for comment in content[i-1].split():
                            comments[comment] = True

                    attributes[attr_for][attr_name] = Attribute(ret_type, **comments)

        i += 1

    return operations, attributes
