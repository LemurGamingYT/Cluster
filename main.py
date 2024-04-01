from subprocess import run as run_sys
from argparse import ArgumentParser
from sys import exit as sys_exit
from pathlib import Path
from typing import Union

from build_utils import build_file, directory_is_project, make_project_configurations, build_project


def get_arg(args_list: list[str], i: int):
    if i < len(args_list):
        return args_list[i]
    else:
        print(f'Argument {i} not found')
        sys_exit(1)


def run_exe(out: Path) -> None:
    try:
        run_sys([f'./{out.as_posix()}'])
    except FileNotFoundError:
        print(f'File {out.as_posix()} not found')


def build(args_list: list[str]) -> None:
    is_project = directory_is_project(Path.cwd())
    if not is_project:
        build_file(Path(get_arg(args_list, 0)))
    else:
        build_project(Path.cwd())

def run(args_list: list[str]) -> None:
    is_project = directory_is_project(Path.cwd())
    out: Union[Path, None] = None
    if not is_project:
        f = Path(get_arg(args_list, 0))
        if f.is_file():
            out = build_file(f)
            if out.suffix in {'.exe', '.'}:
                run_exe(out)
            
                out.unlink()
                f.with_suffix('.cpp').unlink(missing_ok=True)
        elif f.is_dir():
            files = []
            for file in f.rglob('*.cluster'):
                out = build_file(file, should_build=True)
                print(f'Compiled {file.name} to {out.name}')
                files.append(out)
            
            for out in files:
                if out.suffix in {'.exe', '.'}:
                    run_exe(out)
                    
                    out.unlink()
                    f.with_suffix('.cpp').unlink(missing_ok=True)
    else:
        raise NotImplementedError(f'Running a project is not implemented yet')

def init(args_list: list[str]) -> None:
    make_project_configurations(Path.cwd() / get_arg(args_list, 0))


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Cluster compiler')

    arg_parser.add_argument('option', choices=['build', 'run', 'init'],
                            help='Build or run a project/file or initialize a new project')
    arg_parser.add_argument('args', nargs='*', help='Option arguments')

    args = arg_parser.parse_args()

    globals().get(args.option)(args.args)
