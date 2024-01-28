from typing import Any, Iterator, Generator

from more_itertools import peekable

from . import token as tk

IGNORABLE_TOKENS = " \n\t,"
UNMIXABLE_TOKENS = "[](){}\""
MIXABLE_SYMBOLS = ":.`-#"

def scan(it, current_char: str) -> str:
    lexeme = [current_char]

    for char in it:
        is_alphanum = char.isalpha() or char.isdigit()
        is_mixable = char in MIXABLE_SYMBOLS

        if it.peek() in UNMIXABLE_TOKENS + IGNORABLE_TOKENS:
            lexeme.append(char)
            break
        
        if is_alphanum or is_mixable:
            lexeme.append(char)
            continue

        break

    return "".join(lexeme)


def scan_until(it: Iterator[str], start: str, end: str, include_end: bool = False) -> str:
    lexeme = [start]

    for char in it:
        if char == end:
            break
        lexeme.append(char)

    if include_end:
        lexeme.append(end)

    return "".join(lexeme)


def classify(stream: str):
    content_iter = peekable(stream)

    for char in content_iter:

        is_comment_start = char == ";"
        is_block_start = char == "["
        is_block_end = char == "]"
        is_smart_string_start = char == "«"
        is_simple_string_start = char == "\""
        is_char_start = char == "'"
        is_ignorable = char in IGNORABLE_TOKENS

        if is_ignorable:
            continue

        if is_comment_start:
            comment = scan_until(content_iter, char, end="\n")
            yield tk.Token(comment, tk.Kind.Comment)
            continue

        if is_block_start:
            yield tk.Token("[", tk.Kind.OpenBlock)
            continue

        if is_block_end:
            yield tk.Token("]", tk.Kind.CloseBlock)
            continue

        if is_smart_string_start:
            string = scan_until(content_iter, char, end="\n")
            yield tk.Token(string, tk.Kind.String)
            continue

        if is_simple_string_start:
            string = scan_until(content_iter, char, end="\"", include_end=True)
            yield tk.Token(string, tk.Kind.String)
            continue

        if is_char_start:
            _char = scan_until(content_iter, char, end="'", include_end=True)
            yield tk.Token(_char, tk.Kind.Char)
            continue
        
        if (word_or_label := scan(content_iter, char)).endswith(":"):
            yield tk.Token(word_or_label, tk.Kind.Label)
        else:
            yield tk.Token(word_or_label, tk.Kind.Word)
