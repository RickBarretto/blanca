import pytest

import src

def test_block_with_words():
    result = {"languages": [
        "arturo", "python", "ruby"
    ]}

    assert result == src.load("languages: [ arturo python ruby ]")

def test_separation_between_block_and_word():
    result = {"languages": [
        "arturo", "python", "ruby"
    ]}

    assert result == src.load("languages: [arturo python ruby]")

def test_separation_between_block_and_simple_string():
    result = {"languages": [
        "arturo", "python", "ruby"
    ]}

    assert result == src.load("languages: [\"arturo\" \"python\" \"ruby\"]")

def test_label_inside_block_raising_valueerror():
    with pytest.raises(ValueError) as err:
        src.load("languages: [compiled: nim]")

    assert ":label can't be assigned inside a block." == str(err.value)