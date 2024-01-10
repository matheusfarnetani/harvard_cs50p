from response import validate


def test_response():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("email@website.com") == "Valid"
    assert validate("malan@@@harvard.edu") == "Invalid"
    assert validate("email@website..com") == "Invalid"