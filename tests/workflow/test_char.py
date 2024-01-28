
from src import classifier
from src import tokenizer as tk
from src import parser


sample = f"""
a: 'a'
newLine: '\\n'
"""

lexemes = [
    "a:", 
    "'a'",
    "newLine:", 
    "'\\n'"
]

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

def test_basic_lexing():
    for i, lexeme in enumerate(classifier.lex(sample)):
        assert lexemes[i] == lexeme

def test_basic_tokening():
    for i, token in enumerate(tk.tokenize(iter(lexemes))):
        assert tokens[i] == token

def test_basic_parsing():
    assert result == parser.decode(iter(tokens))