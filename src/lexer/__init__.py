from typing import Any, Iterator, Generator

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


def lex(stream: str) -> Generator[str, Any, None]:
    content_iter = iter(stream)

    for char in content_iter:

        is_comment_start = char == ";"
        is_smart_string_start = char == "«"
        is_simple_string_start = char == "\""
        is_ignorable = char in IGNORABLE_TOKENS


        if is_comment_start:
            yield spaced_scan(content_iter, char, end="\n")
        elif is_smart_string_start:
            yield spaced_scan(content_iter, char, end="\n")
        elif is_simple_string_start:
            yield spaced_scan(content_iter, char, end="\"", include_end=True)
        elif is_ignorable:
            continue
        else:
            yield default_scan(content_iter, char)