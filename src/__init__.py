from .import classifier
from .import parser
from .import tokenizer

def load(content: str) -> dict:
    return parser.decode(tokenizer.tokenize(classifier.lex(content)))