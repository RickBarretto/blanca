from src import classifier
from src.classifier import token as tk
from src import decoder


sample = """
from: Arturo
; from: Arturo
to: Python
ext1: art
ext2: py 
"""

tokens = [
    tk.Token("from:", tk.Kind.Label),
    tk.Token("Arturo", tk.Kind.Word),
    tk.Token("; from: Arturo", tk.Kind.Comment),
    tk.Token("to:", tk.Kind.Label),
    tk.Token("Python", tk.Kind.Word),
    tk.Token("ext1:", tk.Kind.Label),
    tk.Token("art", tk.Kind.Word),
    tk.Token("ext2:", tk.Kind.Label),
    tk.Token("py", tk.Kind.Word),
]

result = {
    "from": "Arturo",
    "to": "Python",
    "ext1": "art",
    "ext2": "py",
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
