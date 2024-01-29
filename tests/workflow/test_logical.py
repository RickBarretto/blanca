from src import classifier
from src.classifier import token as tk
from src import decoder


sample = """
true: !true
false: !false
maybe: !maybe
true?: !true
false?: !false
maybe?: !maybe
"""

tokens = [
    tk.Token("true:", tk.Kind.Label),
    tk.Token("!true", tk.Kind.Logical),
    tk.Token("false:", tk.Kind.Label),
    tk.Token("!false", tk.Kind.Logical),
    tk.Token("maybe:", tk.Kind.Label),
    tk.Token("!maybe", tk.Kind.Logical),
 
    tk.Token("true?:", tk.Kind.Label),
    tk.Token("!true", tk.Kind.Logical),
    tk.Token("false?:", tk.Kind.Label),
    tk.Token("!false", tk.Kind.Logical),
    tk.Token("maybe?:", tk.Kind.Label),
    tk.Token("!maybe", tk.Kind.Logical),
]

result = {
    "true": True,
    "false": False,
    "maybe": False,
    "true?": True,
    "false?": False,
    "maybe?": False
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
