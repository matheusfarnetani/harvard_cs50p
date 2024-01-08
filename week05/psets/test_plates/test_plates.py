# Re-requesting a Vanity Plate

from plates import is_valid


def test_is_valid_prefix():
    assert is_valid("12345") == False
    assert is_valid("CS50") == True


def test_is_valid_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("HELLOOOO") == False
    assert is_valid("H") == False
    assert is_valid("HE") == True


def test_is_valid_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_is_valid_punctuation():
    assert is_valid("PI3.14") == False