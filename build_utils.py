from subprocess import run as run_sys
from json import loads, dumps
from platform import system
from shutil import which
from pathlib import Path
from os import makedirs

from antlr4 import CommonTokenStream, FileStream

from compiler.parser.ClusterParser import ClusterParser
from compiler.parser.ClusterLexer import ClusterLexer
from compiler.file_validator import validate_file
from compiler.cpp_info import DEFAULT_HEADER
from compiler import ClusterCompiler


VERSION = '0.0.1'


JSON_DEFAULT = {
    'name': '{}',
    'version': VERSION,
    'main-file': '{}'
}


def directory_is_project(directory: Path) -> bool:
    return (directory / 'cluster.json').exists()

def project_configurations(directory: Path) -> dict:
    if (directory / 'cluster.json').exists():
        return loads((directory / 'cluster.json').read_text())

    return {}

def make_project_configurations(directory: Path) -> None:
    makedirs(directory, exist_ok=True)
    
    json_content = JSON_DEFAULT
    json_content['name'] = directory.name
    json_content['main-file'] = 'src/main.cluster'

    json = (directory / 'cluster.json')
    json.touch()
    json.write_text(dumps(json_content, indent=4))

    src = (directory / 'src')
    makedirs(src, exist_ok=True)
    
    (src / 'main.cluster').write_text("""func main() -> int {
    print("Hello world")
    return 0
}\n""")


def build_project(path: Path) -> Path:
    configurations = project_configurations(path)
    main_file = path / configurations['main-file']
    print(main_file)

def build_to_exe(cpp: Path) -> Path:
    out = cpp.with_suffix('.exe') if system() == 'Windows' else cpp.with_suffix('')
    
    gpp = which('g++')
    if gpp is not None:
        run_sys(['g++', '-o', str(out), str(cpp), '-std=c++17'])
    else:
        clangpp = which('clang++')
        if clangpp is not None:
            run_sys(['clang++', '-o', str(out), str(cpp)])
        else:
            print('No valid C++ compiler found, expected clang++ or g++')
        
    clang_format = which('clang-format')
    if clang_format is not None:
        run_sys(['clang-format', '-i', str(cpp)])
    
    return out

def build_file(file_path: Path, extension: str = '.cpp', should_build: bool = True) -> Path:
    fstream = FileStream(file_path.as_posix(), 'utf-8')

    lexer = ClusterLexer(fstream)
    tokens = CommonTokenStream(lexer)

    parser = ClusterParser(tokens)
    tree = parser.parse()

    compiler = ClusterCompiler(file_path.read_text())
    code = compiler.visitParse(tree)

    src = ''
    for stmt in code:
        src += stmt.code + '\n'

    cpp = file_path.with_suffix(extension)
    include_header = f'#include "{DEFAULT_HEADER.absolute()}"'
    cpp.write_text(validate_file(f'{include_header}\n\n{src}\n', compiler.err))
    
    if should_build:
        return build_to_exe(cpp)

    return cpp
