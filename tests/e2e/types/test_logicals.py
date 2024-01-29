import src


def test_possible_logical_values():
    assert {"bool": True}  == src.load("bool: !true")
    assert {"bool": False} == src.load("bool: !false")
    assert {"bool": False} == src.load("bool: !maybe")

def test_bool_keywords_without_macro():
    assert {"im-not-a-bool": "true"}  == src.load("im-not-a-bool: true")
    assert {"im-not-a-bool": "false"} == src.load("im-not-a-bool: false")
    assert {"im-not-a-bool": "maybe"} == src.load("im-not-a-bool: maybe")