from .import lexer
from .import parser
from .import tokenizer

def load(content: str) -> dict:
    return parser.decode(tokenizer.tokenize(lexer.lex(content)))