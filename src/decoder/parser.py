from typing import Any, Callable, Iterator

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
            raise ValueError(
                ":label can't be assigned inside a block."
            )
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
    if current_token.content.isdigit():
        return int(current_token.content)
    
    raise ValueError(":integer must only contain digits.")

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
        tk.Kind.OpenBlock: parse_block,
        tk.Kind.OpenDictBlock: parse_dictionary,
    }

    return table[kind]