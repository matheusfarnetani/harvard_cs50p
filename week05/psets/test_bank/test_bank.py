# Back to the Bank

from bank import value


def test_value():
    assert value("hello") == 0
    assert value("What's") == 100
    assert value("Hey") == 20