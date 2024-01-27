import pytest

from src import lexer

sample = f"""
from: Arturo
; from: Arturo
to: Python
ext1: art
ext2: py 
"""

output = [
    "from:", "Arturo",
    "; from: Arturo",
    "to:", "Python",
    "ext1:", "art",
    "ext2:", "py" 
]

def test_basic_lexing():
    for i, lexeme in enumerate(lexer.lex(sample)):
        assert output[i] == lexeme

