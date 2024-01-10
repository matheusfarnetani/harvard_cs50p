# Working 9 to 5

from working import convert
import pytest


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"


def test_convert_errors():
    with pytest.raises(ValueError):
        assert convert("9am to 5pm")

    with pytest.raises(ValueError):
        assert convert("9AM to 5PM")

    with pytest.raises(ValueError):
        assert convert("9:00AM to 5:00PM")

    with pytest.raises(ValueError):
        assert convert("9:00am to 5:00pm")

    with pytest.raises(ValueError):
        assert convert("cat")
    
    with pytest.raises(ValueError):
        convert("30:00 AM to 5:30 PM")

    with pytest.raises(ValueError):
        convert("12:80 AM to 5:30 PM")

    with pytest.raises(ValueError):
        convert("12:00 AM to 30:00 PM")

    with pytest.raises(ValueError):
        convert("12:00 AM to 12:80 PM")