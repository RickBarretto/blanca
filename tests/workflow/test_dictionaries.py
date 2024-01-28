

from src import classifier
from src.classifier import token as tk
from src import decoder


sample = f"""
extensions: #[
    arturo: art
    python: py
    ruby: rb
]

languages: #[
    compiled: [cpp c nim rust]
]

blanca: #[
    repository: #[
        author: "RickBarretto"
        firstCommit: 2024
    ]
]

"""

tokens = [
    tk.Token("extensions:", tk.Kind.Label),
    tk.Token("#[", tk.Kind.OpenDictionary),
    tk.Token("arturo", tk.Kind.Label),
    tk.Token("art", tk.Kind.Word),
    tk.Token("python", tk.Kind.Label),
    tk.Token("py", tk.Kind.Word),
    tk.Token("ruby", tk.Kind.Label),
    tk.Token("rb", tk.Kind.Word),
    tk.Token("]", tk.Kind.CloseBlock),

    tk.Token("languages:", tk.Kind.Label),
    tk.Token("#[", tk.Kind.OpenDictionary),
    tk.Token("compiled:", tk.Kind.Label),
    tk.Token("[", tk.Kind.OpenBlock),
    tk.Token("c", tk.Kind.Word),
    tk.Token("nim", tk.Kind.Word),
    tk.Token("rust", tk.Kind.Word),
    tk.Token("]", tk.Kind.CloseBlock),
    
    tk.Token("blanca:", tk.Kind.Label),
    tk.Token("#[", tk.Kind.OpenDictionary),
    tk.Token("repository:", tk.Kind.Label),
    tk.Token("author:", tk.Kind.Label),
    tk.Token("RickBarretto", tk.Kind.String),
    tk.Token("firstCommit:", tk.Kind.Label),
    tk.Token("2024", tk.Kind.Integer),
    tk.Token("#[", tk.Kind.OpenDictionary),
    tk.Token("]", tk.Kind.CloseBlock),

]

result = {
    "extensions": {
        "arturo": "art",
        "python": "py",
        "ruby": "rb"
    },
    
    "languages": {
        "compiled": ["cpp", "c", "nim", "rust"]
    },

    "blanca": {
        "repository": {
            "author": "RickBarretto",
            "firstCommit": 2024
        }
    }
}

def test_basic_tokening():
    for i, token in enumerate(classifier.classify(sample)):
        assert tokens[i] == token

def test_basic_parsing():
    assert result == decoder.decode(iter(tokens))