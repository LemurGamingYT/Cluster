from subprocess import run as run_sys
from json import loads, dumps
from platform import system
from shutil import which
from pathlib import Path
from os import makedirs

from compiler import ClusterCompiler


VERSION = '0.0.2'


JSON_DEFAULT = {
    'name': '{}',
    'version': VERSION,
    'main-file': '{}'
}


def make_into_exe(file: Path) -> Path:
    return file.with_suffix('.exe') if system() == 'Windows' else file.with_suffix('')

def directory_is_project(directory: Path) -> bool:
    return (directory / 'cluster.json').exists()

def project_configurations(directory: Path) -> dict:
    if (directory / 'cluster.json').exists():
        return loads((directory / 'cluster.json').read_text())

    return {}

def make_project_configurations(directory: Path) -> None:
    makedirs(directory, exist_ok=True)

    json_content = JSON_DEFAULT.copy()
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


def build_project(path: Path, should_build: bool = True) -> Path:
    configurations = project_configurations(path)
    main_file: Path = path / configurations.get('main-file')
    if main_file is None or not main_file.exists():
        print(f'Main File ({main_file.as_posix()}) not found')
    elif main_file.is_dir():
        print(f'Main File ({main_file.as_posix()}) is a directory, expected a file')

    for file in path.rglob('*.cluster'):
        if file.absolute() == main_file.absolute():
            continue

        build_file(file, '.hpp', False)

    main = build_file(main_file, should_build=should_build)
    name = configurations.get('name')
    if name is not None:
        main.rename(path / make_into_exe(Path(name)))

    return main

def build_to_exe(cpp: Path) -> Path:
    out = make_into_exe(cpp)

    if which('g++') is not None:
        run_sys(['g++', '-o', str(out), str(cpp)])
    elif which('clang++') is not None:
        run_sys(['clang++', '-o', str(out), str(cpp)])
    else:
        print('No valid C++ compiler found, expected clang++ or g++')

    if which('clang-format') is not None:
        run_sys(['clang-format', '-i', str(cpp)])
    
    return out

def build_file(file_path: Path, extension: str = '.cpp', should_build: bool = True) -> Path:
    if file_path.suffix == '.cluster':
        compiler = ClusterCompiler(file_path)
        cpp = compiler.compile(file_path, extension)

        if should_build:
            return build_to_exe(cpp)

        return cpp
    elif file_path.suffix == '.cpp':
        return build_to_exe(file_path)
