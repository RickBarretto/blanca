from src import classifier
from src.classifier import token as tk
from src import decoder


sample = """
blue: #blue
color2: #0077BB
"""

tokens = [
    tk.Token("blue:", tk.Kind.Label),
    tk.Token("#blue", tk.Kind.Color),
    tk.Token("color2:", tk.Kind.Label),
    tk.Token("#0077BB", tk.Kind.Color),
]

result = {
    "blue": "blue",
    "color2": "#0077bb"
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
