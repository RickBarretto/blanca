from typing import Any, Iterator, Generator

from . import token as tk

IGNORABLE_TOKENS = " \n\t,"
MIXABLE_SYMBOLS = ":.`-#"

def default_scan(it: Iterator[str], current_char: str) -> str:
    lexeme = [current_char]

    for char in it:
        is_alphanum = char.isalpha() or char.isdigit()
        is_mixable = char in MIXABLE_SYMBOLS

        if (not is_alphanum) and (not is_mixable):
            break
        lexeme.append(char)

    return "".join(lexeme)


def spaced_scan(it: Iterator[str], start: str, end: str, include_end: bool = False) -> str:
    lexeme = [start]

    for char in it:
        if char == end:
            break
        lexeme.append(char)

    if include_end:
        lexeme.append(end)

    return "".join(lexeme)


def lex(stream: str):
    content_iter = iter(stream)

    for char in content_iter:

        is_comment_start = char == ";"
        is_smart_string_start = char == "«"
        is_simple_string_start = char == "\""
        is_char_start = char == "'"
        is_ignorable = char in IGNORABLE_TOKENS

        if is_ignorable:
            continue

        if is_comment_start:
            comment = spaced_scan(content_iter, char, end="\n")
            yield tk.Token(comment, tk.Kind.Comment)
            continue

        if is_smart_string_start:
            string = spaced_scan(content_iter, char, end="\n")
            yield tk.Token(string, tk.Kind.String)
            continue

        if is_simple_string_start:
            string = spaced_scan(content_iter, char, end="\"", include_end=True)
            yield tk.Token(string, tk.Kind.String)
            continue

        if is_char_start:
            _char = spaced_scan(content_iter, char, end="'", include_end=True)
            yield tk.Token(_char, tk.Kind.Char)
            continue
        
        if (word_or_label := default_scan(content_iter, char)).endswith(":"):
            yield tk.Token(word_or_label, tk.Kind.Label)
        else:
            yield tk.Token(word_or_label, tk.Kind.Word)
