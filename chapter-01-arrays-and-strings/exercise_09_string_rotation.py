"""
Assume you have method is_substring, give two strings s1 and s2 write code to check if s2 is rotation of s1 using only one call to is_substring
"""
import pytest


def is_substring(s1, s2):
    return s1 in s2


def string_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s1 in f"{s2}{s2}"


@pytest.fixture(
    params=[
        string_rotation,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("waterbottle", "erbottlewat", True),
        ("waterbottle", "erbotelewat", False),
        ("abab", "ab", False),
        ("lorem", "lorem", True),
    ],
)
def test_string_rotation(s1, s2, expected, function_under_test):
    assert function_under_test(s1, s2) == expected


if __name__ == "__main__":
    print(f"{string_rotation('waterbottle')=}")
