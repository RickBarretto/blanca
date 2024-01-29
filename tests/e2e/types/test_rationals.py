import src


def test_simple_rational():
    assert {"number": (4, 5)} == src.load("number: 4:5")


def test_rational_starting_with_0():
    """Numbers beginning with 0s should also be considered as numbers.

    The 0s at the beginning should not be considered thought of as data,
    so, they must be truncated at decoder level.
    """
    assert {"number": (2, 3)} == src.load("number: 2:003")
    assert {"number": (2, 3)} == src.load("number: 0002:3")
    assert {"number": (2, 3)} == src.load("number: 002:003")

def test_rational_division_by_zero():
    # this is just data representation, so should be 100% possible
    assert {"number": (0, 0)} == src.load("number: 0:0")