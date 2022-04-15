"""
Implement a method to perform basic string compression using the counts of repeated characters
"""
import typing as t

import pytest


def count_letters(input: str) -> t.Iterator[tuple[str, int]]:
    """
    allwed input: a-zA-Z, so it's possible to use # as fillter
    """
    count = 1
    for current, next in zip(input, input[1:] + "#"):
        if current == next:
            count += 1
        else:
            yield current, count
            count = 1


def string_compression(input: str):
    return "".join(
        f"{letter}{count}" if count > 1 else letter
        for (letter, count) in count_letters(input)
    )


@pytest.fixture(
    params=[
        string_compression,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "input,expected",
    [
        ("aabcccccaaa", "a2bc5a3"),
    ],
)
def test_string_compression(input, expected, function_under_test):
    assert function_under_test(input) == expected


if __name__ == "__main__":
    print(f"{string_compression('')=}")
