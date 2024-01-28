import pytest

import src

def test_dict_with_words():
    result = {
        "languages": {
            "compiled": ["c", "cpp", "rust"],
            "interpreted": ["arturo", "python"]
        } 
    }

    assert result == src.load(
        """
        languages: #[ 
            compiled: [c cpp rust]
            interpreted: [arturo python] 
        ]                      
        """
    )

def test_separation_between_dict_block_and_label():
    result = {"testing": {"key": "value"}}

    assert result == src.load("testing: #[key: value]")

def test_empty_dict():
    result = { "empty": {}}
    assert result == src.load("empty: #[]")

def test_nested_dict():
    result = {
        "surface": {"level1": {"level2": {}}}
    }

    assert result == src.load(
        """
        surface: #[level1: #[level2: #[]]]
        """
    )


def test_missing_label_inside_dict_block_raising_valueerror():
    with pytest.raises(ValueError) as err:
        src.load("languages: #[compiled nim]")

    assert "Values inside :dictionary must be paired as [:label :any]" == str(err.value)