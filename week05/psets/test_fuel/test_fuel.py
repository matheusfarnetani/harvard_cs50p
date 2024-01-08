# Refueling

import pytest
from fuel import convert, gauge


def test_convert_fractions():
    assert convert("4/4") == 100
    assert convert("3/4") == 75
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("0/4") == 0

    # with pytest.raises(SystemExit) as pr:
    #     convert("5/4")
    # assert pr.type == SystemExit
    # assert pr.value.code == "Fraction value is more than 100%"


def test_convert_zeros():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_convert_strings():
    with pytest.raises(ValueError):
        convert("test/test")
    with pytest.raises(ValueError):
        convert("cat/5")
    with pytest.raises(ValueError):
        convert("5/dog")


# def test_convert_phrase():
#     with pytest.raises(SystemExit) as pr:
#         convert("What should I do?")
#     assert pr.type == SystemExit
#     assert pr.value.code == 1


def test_gauge():
    for i in range(0, 101):
        if i <= 1:
            assert gauge(i) == "E"
        elif 99 <= i <= 100:
            assert gauge(i) == "F"
        else:
            assert gauge(i) == f"{i}%"