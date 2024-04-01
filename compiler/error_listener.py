from typing import Callable, NoReturn

from antlr4.error.ErrorListener import ErrorListener


class ClusterErrorListener(ErrorListener):
    def __init__(self, src: str, errorfn: Callable[[str, str, tuple[int, int]], NoReturn]) -> None:
        self.err = errorfn
        self.src = src
    
    def syntaxError(self, _, offendingSymbol, line, column, msg, e) -> None:
        self.err(
            'Syntax',
            f'Invalid syntax \'{offendingSymbol.text}\' at ln {line}, col {column}',
            (line, column)
        )
