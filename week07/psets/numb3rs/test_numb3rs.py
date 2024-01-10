# NUMB3RS

from numb3rs import validate


def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True


def test_validate_onlydigits():
    assert validate("cat") == False
    assert validate("!@#") == False


def test_validate_ndigits():
    assert validate("1.1.1.1") == True
    assert validate("10.10.10.10") == True
    assert validate("100.100.100.100") == True
    assert validate("1000.1000.1000.1000") == False
    assert validate("1") == False
    assert validate("1.1") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False


def test_validate_limit():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False


def test_validate_dots():
    assert validate("-256.0.0.0") == False
    assert validate("0.-256.0.0") == False
    assert validate("0.0.-256.0") == False
    assert validate("0.0.0.-256") == False
