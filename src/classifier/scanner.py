from typing import Iterator

IGNORABLE_TOKENS = " \n\t,"
UNMIXABLE_TOKENS = "[](){}\""
MIXABLE_SYMBOLS = ":.`-#"

def scan(it, current_char: str) -> str:
    lexeme = [current_char]

    for char in it:
        is_alphanum = char.isalpha() or char.isdigit()
        is_mixable = char in MIXABLE_SYMBOLS

        if it.peek(" ") in UNMIXABLE_TOKENS + IGNORABLE_TOKENS:
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