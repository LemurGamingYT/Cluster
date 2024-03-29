from typing import Callable, NoReturn

from compiler.cpp_info import DEFAULT_HEADER


def validate_file(src: str, errorfn: Callable[[str, str, tuple[int, int]], NoReturn]) -> str:
    has_include = False
    has_main_function = False
    
    indentation = ''
    
    new_source = ''
    lines = src.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line == f'#include "{DEFAULT_HEADER.absolute()}"':
            has_include = True
            new_source += line + '\n'
        elif line == 'int_t main() {':
            has_main_function = True
            new_source += 'int main() {\n'
            indentation += ' ' * 4
            for body_length, stmt in enumerate(lines[i+1:]):
                if stmt == 'return (int_t)0':
                    new_source += f'{indentation}return 0;\n'
                elif stmt == '}':
                    indentation = indentation[:-4]
                    new_source += f'{indentation}}}\n'
                    break
                else:
                    new_source += f'{indentation}{stmt};\n'

            i += body_length + 1
        elif line == '':
            new_source += line + '\n'
        else:
            new_source += line + ';\n'

        i += 1

    if not has_include:
        print('Something went wrong with compilation and no default include was found, adding')
        new_source = f'#include "{DEFAULT_HEADER.absolute()}"\n\n{new_source}'
    
    if not has_main_function:
        errorfn('Compile', f'No main function found in file', (1, 1))

    return new_source
