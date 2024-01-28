from .import classifier
from .import parser

def load(content: str) -> dict:
    return parser.decode(classifier.lex(content))