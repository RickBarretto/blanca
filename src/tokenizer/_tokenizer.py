from typing import Iterable
from .token import Token, Kind

def tokenize(lexeme_stream: Iterable[str]):

    for lexeme in lexeme_stream:
        if lexeme.startswith(";"):
            yield Token(lexeme, Kind.Comment)
        elif lexeme.endswith(":"):
            yield Token(lexeme, Kind.Label)
        elif lexeme.startswith("\"") and lexeme.endswith("\""):
            yield Token(lexeme, Kind.String)
        elif lexeme.startswith("'") and lexeme.endswith("'"):
            yield Token(lexeme, Kind.Char)
        else:
            yield Token(lexeme, Kind.Word)
        