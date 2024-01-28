from typing import Iterator

from src.classifier import token as tk

from . import _parser

def parse_tokens(it: Iterator[tk.Token]):
    for token in it:
        if token.kind == tk.Kind.Comment:
            continue

        if token.kind == tk.Kind.Label:
            yield token.content[:-1], _parser.parse_label(it)


def decode(it):
    return {key: val for key, val in parse_tokens(it)}