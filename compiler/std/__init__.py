from pathlib import Path


LIBRARIES = {
    'fstream': (Path(__file__).parent / 'fstream.hpp').as_posix(),
    'time': (Path(__file__).parent / 'time.hpp').as_posix(),
    # 'knock': (Path(__file__).parent / 'knock.hpp').as_posix(),
    'process': (Path(__file__).parent / 'process.hpp').as_posix(),
    # 'mem': (Path(__file__).parent / 'mem.hpp').as_posix(),
    'lcode': (Path(__file__).parent / 'lcode.hpp').as_posix(),
}
