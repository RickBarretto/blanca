import src


def test_simple_floating():
    assert {"number": 10.55} == src.load("number: 10.55")

def test_floating_0():
    assert {"number": 0.0} == src.load("number: 0.0")

def test_simple_floating_starting_with_0():
    """Numbers beginning with 0s should also be considered as numbers.

    The 0s at the beginning should not be considered thought of as data,
    so, they must be truncated at decoder level.
    """
    assert {"number": 101.0} == src.load("number: 000000101.0")
