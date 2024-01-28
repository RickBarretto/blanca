from src import classifier
from src.classifier import token as tk
from src import decoder


sample = f"""
age: 30
year: 2024
"""

tokens = [
    tk.Token("age:", tk.Kind.Label),
    tk.Token("30", tk.Kind.Integer),
    tk.Token("year:", tk.Kind.Label),
    tk.Token("2024", tk.Kind.Integer),
]

result = {
    "age": 30,
    "year": 2024,
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
