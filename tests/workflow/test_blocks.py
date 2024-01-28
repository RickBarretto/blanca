from src import classifier
from src.classifier import token as tk
from src import decoder


sample = """
vms: [
    arturo,
    python,
    ruby
]

compiled: [c nim rust]

ext: [
    [art py rb],
    [c nim rs],
]

"""

tokens = [
    tk.Token("vms:", tk.Kind.Label),
    tk.Token("[", tk.Kind.OpenBlock),
    tk.Token("arturo", tk.Kind.Word),
    tk.Token("python", tk.Kind.Word),
    tk.Token("ruby", tk.Kind.Word),
    tk.Token("]", tk.Kind.CloseBlock),
    tk.Token("compiled:", tk.Kind.Label),
    tk.Token("[", tk.Kind.OpenBlock),
    tk.Token("c", tk.Kind.Word),
    tk.Token("nim", tk.Kind.Word),
    tk.Token("rust", tk.Kind.Word),
    tk.Token("]", tk.Kind.CloseBlock),
    tk.Token("ext:", tk.Kind.Label),
    tk.Token("[", tk.Kind.OpenBlock),
    tk.Token("[", tk.Kind.OpenBlock),
    tk.Token("art", tk.Kind.Word),
    tk.Token("py", tk.Kind.Word),
    tk.Token("rb", tk.Kind.Word),
    tk.Token("]", tk.Kind.CloseBlock),
    tk.Token("[", tk.Kind.OpenBlock),
    tk.Token("c", tk.Kind.Word),
    tk.Token("nim", tk.Kind.Word),
    tk.Token("rs", tk.Kind.Word),
    tk.Token("]", tk.Kind.CloseBlock),
    tk.Token("]", tk.Kind.CloseBlock),
]

result = {
    "vms": ["arturo", "python", "ruby"],
    "compiled": ["c", "nim", "rust"],
    "ext": [
        ["art", "py", "rb"],
        ["c", "nim", "rs"],
    ],
}


def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token


def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))
