"""
Implement an algorithm to determine if a string hasll all unique characters
"""
import pytest


def is_unique(input: str) -> bool:
    """simple version"""
    while input:
        needle, *input = input
        if needle in input:
            return False
    return True


def is_unique_ascii(input: str) -> bool:
    """ascii version of is unique. Assume input string is ascii"""
    letters = list(input.encode())
    in_string = [False for _ in range(256)]
    for letter in letters:
        if in_string[letter]:
            return False
        in_string[letter] = True
    return True


params = [("", True), ("a", True), ("abc", True), ("abca", False)]


@pytest.fixture(params=[is_unique, is_unique_ascii])
def function_under_test(request):
    return request.param


@pytest.mark.parametrize("input,expected", params)
def test_is_unique(input, expected, function_under_test):
    assert function_under_test(input) == expected


if __name__ == "__main__":
    print(is_unique("abcdefgqac"))
