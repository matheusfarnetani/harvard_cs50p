from um import count


def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2