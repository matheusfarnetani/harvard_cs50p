# Seasons of Love

from datetime import date, timedelta
from seasons import validate, calculate, convert_to_words
import pytest


def test_validate():
    assert validate("2023-01-10") == date(2023,1,10)
    assert validate("2022-01-10") == date(2022,1,10)

    with pytest.raises(SystemExit) as pr:
        validate("01-10-2023")
    assert pr.type == SystemExit
    assert pr.value.code == 1


def test_calculate():
    assert calculate(date.today()-timedelta(days=365)) == 525600
    assert calculate(date.today()-timedelta(days=730)) == 1051200


def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"