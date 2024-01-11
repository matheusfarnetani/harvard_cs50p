# Cookie Jar

import pytest
from jar import Jar


def test_init():
    j = Jar()
    with pytest.raises(ValueError):
        j.capacity = -1
    with pytest.raises(ValueError):
        j.capacity = "a"
    with pytest.raises(ValueError):
        j.size = -1
    with pytest.raises(ValueError):
        j.size = "a"


def test_str():
    j = Jar()
    assert str(j) == ""
    j.deposit(1)
    assert str(j) == "🍪"
    j.deposit(11)
    assert str(j) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0
    with pytest.raises(ValueError):
        j.deposit(13)
    with pytest.raises(ValueError):
        j.deposit(-13)
    with pytest.raises(ValueError):
        j.withdraw(1)
    with pytest.raises(ValueError):
        j.withdraw(-1)
    with pytest.raises(ValueError):
        j.withdraw("a")

def test_withdraw():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0
    with pytest.raises(ValueError):
        j.withdraw(-1)
    with pytest.raises(ValueError):
        j.withdraw("a")
    with pytest.raises(ValueError):
        j.withdraw(13)