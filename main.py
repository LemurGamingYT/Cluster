from subprocess import run as run_sys
from argparse import ArgumentParser
from pathlib import Path
from typing import Union

from build_utils import build_file, directory_is_project, make_project_configurations


def build(args_list: list[str]) -> None:
    is_project = directory_is_project(Path.cwd())
    if not is_project:
        build_file(Path(args_list[0]), should_build=True)

def run(args_list: list[str]) -> None:
    is_project = directory_is_project(Path.cwd())
    out: Union[Path, None] = None
    if not is_project:
        out = build_file(Path(args_list[0]), should_build=True)
        if out.suffix in {'.exe', '.'}:
            run_sys([f'./{out.as_posix()}'])

            if out is not None:
                out.unlink()
                out.with_suffix('.cpp').unlink()

def init(args_list: list[str]) -> None:
    make_project_configurations(Path.cwd() / args_list[0])


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Cluster compiler')

    arg_parser.add_argument('option', choices=['build', 'run', 'init'], help='Build or run')
    arg_parser.add_argument('args', nargs='*', help='Option arguments')

    args = arg_parser.parse_args()

    globals().get(args.option)(args.args)
