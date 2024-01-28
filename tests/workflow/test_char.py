
from src import classifier
from src.classifier import token as tk
from src import parser


sample = f"""
a: 'a'
newLine: '\\n'
"""

tokens = [
    tk.Token("a:",          tk.Kind.Label),
    tk.Token("'a'",         tk.Kind.Char),
    tk.Token("newLine:",    tk.Kind.Label),
    tk.Token("'\\n'",       tk.Kind.Char),
]

result = {
    "a": "a",
    "newLine": "\n"
}

def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token

def test_basic_parsing():
    assert result == parser.decode(iter(tokens))