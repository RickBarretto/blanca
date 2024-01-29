from typing import Callable, Iterator
import importlib
import string

from src.classifier import token as tk


def parse_label(it: Iterator[tk.Token]):
    try:
        next_tk = next(it)
    except StopIteration:
        raise ValueError("There is no value to be assigned") from StopIteration

    if next_tk.kind == tk.Kind.Label:
        raise ValueError("You can't assing a Label with another label")

    return token_table(next_tk.kind)(it, next_tk)


def parse_block(it: Iterator[tk.Token], next_tk: tk.Token):
    result = []
    for token in it:
        if token.kind == tk.Kind.CloseBlock:
            break
        if token.kind == tk.Kind.Label:
            raise ValueError(":label can't be assigned inside a block.")
        result.append(token_table(token.kind)(it, token))

    return result


def parse_dictionary(it: Iterator[tk.Token], next_tk: tk.Token):
    result = {}
    for token in it:
        if token.kind == tk.Kind.CloseBlock:
            break
        if token.kind != tk.Kind.Label:
            raise ValueError(
                "Values inside :dictionary must be paired as [:label :any]"
            )

        key = token.content[:-1]
        result[key] = parse_label(it)

    return result


def parse_word(it: Iterator[tk.Token], current_token: tk.Token):
    return current_token.content


def parse_string(it: Iterator[tk.Token], current_token: tk.Token):
    return current_token.content[1:-1]


def parse_integer(it: Iterator[tk.Token], current_token: tk.Token):
    # Ignores the dot at the end
    content = current_token.content
    integer = content[:-1] if content.endswith(".") else content
    
    if integer.isdigit():
        return int(integer)

    raise ValueError(":integer must only contain digits.")


def parse_floating(it: Iterator[tk.Token], current_token: tk.Token):
    for ch in current_token.content:
        if ch.isdigit():
            continue
        if ch == ".":
            continue

        raise ValueError(":floating must only contain digits and one dot.")

    return float(current_token.content)

def parse_rational(it: Iterator[tk.Token], current_token: tk.Token):
    for ch in current_token.content:
        if ch.isdigit():
            continue
        if ch == ":":
            continue

        raise ValueError(":rational must only contain digits and one colon.")

    den, num = current_token.content.split(":")
    return int(den), int(num)

def parse_logical(it: Iterator[tk.Token], current_token: tk.Token):
    if current_token.content == "!true":
        return True
    
    if current_token.content in ("!false", "!maybe"):
        return False
    
    raise ValueError(f"Unknown :logical type: {current_token.content}")

def parse_color(it: Iterator[tk.Token], current_token: tk.Token):
    colors = importlib.import_module("src.decoder.colors")
    error_msg = f"Unknown color: {current_token.content}"

    def remove_case(color: str):
        return color.replace("-", "").replace("_", "").lower()

    color = remove_case(current_token.content)

    if color[1:] in colors.color_names:
        return color[1:]
    
    if len(color) not in (4, 7):
        raise ValueError(error_msg)

    for digit in color[1:]:
        if digit not in string.hexdigits:
            raise ValueError(error_msg)

    return color.lower()


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
        tk.Kind.Integer: parse_integer,
        tk.Kind.Floating: parse_floating,
        tk.Kind.Rational: parse_rational,
        tk.Kind.Logical: parse_logical,
        tk.Kind.Color: parse_color,
        tk.Kind.OpenBlock: parse_block,
        tk.Kind.OpenDictBlock: parse_dictionary,
    }

    return table[kind]
