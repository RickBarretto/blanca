from dataclasses import dataclass
from typing import Any, Callable, Generator, Iterable, Iterator

from src.classifier import token as tk

from . import node

def parse_label(it: Iterator[tk.Token]):    
    try:
        next_tk = next(it)
    except StopIteration:
        raise ValueError("There is no value to be assigned") from StopIteration

    if next_tk.kind == tk.Kind.Label:
        raise ValueError("You can't assing a Label with another label")
    
    return token_table(next_tk.kind)(it, next_tk)


def parse_word(it: Iterator[tk.Token], current_token: tk.Token):
    return current_token.content

def parse_string(it: Iterator[tk.Token], current_token: tk.Token):
    return current_token.content[1:-1]

def parse_char(it: Iterator[tk.Token], current_token: tk.Token):
    content = current_token.content

    has_one_char = 3 == len(content)
    has_two_char_representing_one = (4 == len(content)) and (content[1] == "\\")

    if has_one_char:
        return current_token.content[1:-1]

    if has_two_char_representing_one:
        convertion = {
            "\\n": "\n",
            "\\t": "\t",
            "\\r": "\r",
            "\\f": "\f",
            "\\a": "\a",
            "\\b": "\b",
            "\\v": "\v",
        }
        char = current_token.content[1:-1]
        try:
            return convertion[char]
        except KeyError:
            return char
                                          
    raise ValueError("A :char should contain only one character.")

    

def token_table(kind: tk.Kind) -> Callable:
    table = {
        tk.Kind.Label: parse_label,
        tk.Kind.Word: parse_word,
        tk.Kind.String: parse_string,
        tk.Kind.Char: parse_char,
    }

    return table[kind]


def parse_tokens(it: Iterator[tk.Token]):
    for token in it:
        if token.kind == tk.Kind.Comment:
            continue

        if token.kind == tk.Kind.Label:
            yield token.content[:-1], parse_label(it)


def decode(it):
    return {key: val for key, val in parse_tokens(it)}