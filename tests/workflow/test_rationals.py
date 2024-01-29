from src import classifier
from src.classifier import token as tk
from src import decoder


sample = """
rat: 3:5
rat2: 1:4
"""

tokens = [
    tk.Token("rat:", tk.Kind.Label),
    tk.Token("3:5", tk.Kind.Integer),
    tk.Token("rat2:", tk.Kind.Label),
    tk.Token("1:4", tk.Kind.Integer),
]

result = {
    "rat": (3, 5),
    "rat2": (1, 4),
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
