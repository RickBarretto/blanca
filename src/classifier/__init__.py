from more_itertools import peekable

from . import token as tk
from . import scanner


def classify(stream: str):
    content_iter = peekable(stream)

    for char in content_iter:

        is_comment_start = char == ";"
        is_block_start = char == "["
        is_block_end = char == "]"
        is_smart_string_start = char == "«"
        is_simple_string_start = char == "\""
        is_char_start = char == "'"
        is_ignorable = char in scanner.IGNORABLE_TOKENS
        is_number_start = char.isdigit()

        if is_ignorable:
            continue

        if is_comment_start:
            comment = scanner.scan_until(content_iter, char, end="\n")
            yield tk.Token(comment, tk.Kind.Comment)
            continue

        if is_block_start:
            yield tk.Token("[", tk.Kind.OpenBlock)
            continue

        if is_block_end:
            yield tk.Token("]", tk.Kind.CloseBlock)
            continue

        if is_smart_string_start:
            string = scanner.scan_until(content_iter, char, end="\n")
            yield tk.Token(string, tk.Kind.String)
            continue

        if is_simple_string_start:
            string = scanner.scan_until(content_iter, char, end="\"", include_end=True)
            yield tk.Token(string, tk.Kind.String)
            continue

        if is_char_start:
            _char = scanner.scan_until(content_iter, char, end="'", include_end=True)
            yield tk.Token(_char, tk.Kind.Char)
            continue

        if is_number_start:
            number = scan(content_iter, char)
            yield tk.Token(number, tk.Kind.Integer)
            continue
        
        if (word_or_label := scanner.scan(content_iter, char)).endswith(":"):
            yield tk.Token(word_or_label, tk.Kind.Label)
        else:
            yield tk.Token(word_or_label, tk.Kind.Word)
