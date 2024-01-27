import src

def test_simple_string():
    assert {"name": "Joe Doe"} == src.load("name: \"Joe Doe\"")

def test_word_between_simple_strings():
    assert {"name": ""} == src.load("name: \"\"Joe\"\"")