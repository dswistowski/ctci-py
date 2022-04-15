"""
Given two strings, write a method to decide if one is a permutaiton of other
"""
import pytest


def check_permutation(a: str, b: str) -> bool:
    return _check_permutation(list(a), list(b))


def _check_permutation(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    if len(a) <= 1:
        return a == b
    c_a, *sub_a = a

    for i, c_b in enumerate(b):
        if c_b == c_a:
            sub_b = b[:i] + b[i + 1 :]
            return check_permutation(sub_a, sub_b)
    return False


def check_permutation_ascii(a: str, b: str) -> bool:
    return _check_permutation(list(a.encode()), list(b.encode()))


def _check_permutation_ascii(a: list[int], b: list[int]) -> bool:
    counter = [0 for _ in range(256)]
    for n in a:
        counter[n] += 1
    for n in b:
        counter[n] -= 1

    for letter_count in counter:
        if letter_count != 0:
            return False
    return True


@pytest.fixture(params=[check_permutation, check_permutation_ascii])
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("", "", True),
        ("a", "b", False),
        ("a", "a", True),
        ("aa", "a", False),
        ("aaaaaaaaa", "aaaaaaaaa", True),
        ("aaaaaaaaa", "aaaavaaaa", False),
        (
            "adsfwfawepfewjfasdfasdjfslkfjqwlekfjlkdafjgald",
            "fedafdkwakkfjafflfsffpwslwsjalafwedqdjadjjegsl",
            True,
        ),
        (
            "adsfwfawepfewjfasdfasdjfslkfjqwlekfjlkdafjgald",
            "fedafdkwakkfjafflfsfspwslwsjalafwedqdjadjjegsl",
            False,
        ),
    ],
)
def test_check_permutation(a, b, expected):
    assert check_permutation(a, b) == expected


if __name__ == "__main__":
    check_permutation("aaaaaaaaa", "aaaaaaaaa")
