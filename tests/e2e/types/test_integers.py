import src

def test_simple_integer():
    assert {"number": 10} == src.load("number: 10")

def test_simple_integer_starting_with_0():
    """Numbers beginning with 0s should also be considered as numbers.
    
    The 0s at the beginning should not be considered thought of as data,
    so, they must be truncated at decoder level.
    """
    assert {"number": 1010} == src.load("number: 0000001010")