from src import classifier
from src.classifier import token as tk
from src import decoder


sample = """
health: 89.5
velocity: 70.15
"""

tokens = [
    tk.Token("health:", tk.Kind.Label),
    tk.Token("89.5", tk.Kind.Floating),
    tk.Token("velocity:", tk.Kind.Label),
    tk.Token("70.15", tk.Kind.Floating),
]

result = {
    "health": 89.5,
    "velocity": 70.15,
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
