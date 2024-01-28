import src


def test_simple_integer():
    assert {"number": 10} == src.load("number: 10")


def test_simple_integer_starting_with_0():
    """Numbers beginning with 0s should also be considered as numbers.

    The 0s at the beginning should not be considered thought of as data,
    so, they must be truncated at decoder level.
    """
    assert {"number": 1010} == src.load("number: 0000001010")

def test_integer_followed_by_dot():
    """Integer followed by dot should be considered as an :integer.

    Differently from Python, that this would be considered a float,
    in arturo, this is considered an ``:integer``.

    Have a look at the examples bellow:
    
    Example
    =======

    Arturo's Repl
    -------------

        $> inspect 1.
        1 :integer

    Python's Repl
    -------------

        >>> 1.
        1.0
    """
    assert {"number": 1} == src.load("number: 1.")