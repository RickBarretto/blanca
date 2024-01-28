import pytest

import src

def test_simple_char():
    assert {"letter": "a"} == src.load("letter: 'a'")

def test_new_line_char():
    assert {"newLine": "\n"} == src.load("newLine: '\\n'")

def test_more_than_one_non_escapable_char():
    with pytest.raises(ValueError) as err:
        src.load("newLine: 'ab'")

    assert "A :char should contain only one character." == str(err.value)