from lines import count_lines_of_code


def test_count_lines():
    assert count_lines_of_code("../../examples/names4.py") == 3
    assert count_lines_of_code("../../examples/names5.py") == 4
    assert count_lines_of_code("../../examples/names6.py") == 3
    assert count_lines_of_code("../../examples/names7.py") == 6