"""
Implement an algorithm to determine if a string hasll all unique characters
"""
import pytest


def is_unique(input: str):
    while input:
        needle, *input = input
        if needle in input:
            return False
    return True


@pytest.mark.parametrize("input,expected", [
    ('', True),
    ('a', True),
    ('abc', True),
    ('abca', False)
])
def test_is_unique(input, expected):
    assert is_unique(input) == expected


if __name__ == "__main__":
    print(is_unique("abcdefgqac"))
