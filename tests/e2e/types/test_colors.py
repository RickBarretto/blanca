import pytest

import src


def test_simple_named_color():
    assert {"color": "red"} == src.load("color: #red")


def test_invalid_named_color():
    with pytest.raises(ValueError) as err:
        src.load("color: #redd")

    assert "Unknown color: #redd" == str(err.value)


def test_differents_cases_for_named_colors():
    kebab = "blue-diamond"
    snake = "blue_diamond"
    camel = "blueDiamond"
    pascal = "BlueDiamond"

    for color_name in [kebab, snake, camel, pascal]:
        assert {"color": "bluediamond"} == src.load(f"color: #{color_name}")


def test_simple_hex_color():
    assert {"number": 1010} == src.load("number: 0000001010")


def test_invalid_hex_color():
    assert {"number": 1010} == src.load("number: 0000001010")


def test_differents_cases_for_hex_color():
    upper = "0077BB"
    lower = "0077bb"
    mixed1 = "0077Bb"
    mixed2 = "0077bB"

    for hex_color in [upper, lower, mixed1, mixed2]:
        assert {"color": "#0077bb"} == src.load(f"color: #{hex_color}")