"""
Given an image represented bty an N x N matrix where each pixel in the image is represented by integer,
write a method to rotate thre image by 90 degrees
"""
from copy import copy
import typing as t

import pytest


def move(iter: t.Iterable[tuple[int, int]], shift: int):
    for x, y in iter:
        yield x + shift, y + shift


def quarters(pos, size):
    yield pos, 0
    yield 0, size - pos - 1
    yield size - pos - 1, size - 1
    yield size - 1, pos


def rotate_matrix(matrix):
    size = len(matrix)

    for layer in range(size // 2):
        current_size = size - layer * 2
        for i in range(current_size - 1):
            (x1, y1), (x2, y2), (x3, y3), (x4, y4) = move(
                quarters(i, current_size), layer
            )
            matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = (
                matrix[x2][y2],
                matrix[x3][y3],
                matrix[x4][y4],
                matrix[x1][y1],
            )

    return matrix


@pytest.fixture(
    params=[
        rotate_matrix,
    ]
)
def function_under_test(request):
    return request.param


s1 = [list("ab"), list("cd")]
s2 = [list("bd"), list("ac")]

m1 = [
    list("abc"),
    list("abc"),
    list("abc"),
]
m2 = [list("ccc"), list("bbb"), list("aaa")]
m3 = [
    list("abcd"),
    list("efgh"),
    list("ijkl"),
    list("mnop"),
]
m4 = [list("dhlp"), list("cgko"), list("bfjn"), list("aeim")]


@pytest.mark.parametrize(
    "input,expected",
    [
        (s1, s2),
        (m1, m2),
        (m3, m4),
    ],
)
def test_rotate_matrix(input, expected, function_under_test):
    input = copy(input)
    function_under_test(input)
    assert input == expected


@pytest.mark.parametrize(
    "input",
    [s1, m1, m2, m3, m4],
)
def test_rotate_matrix_stable(input):
    original = copy(input)
    input = copy(input)
    for _ in range(4):
        rotate_matrix(input)

    assert input == original
    assert id(input) != id(original)


if __name__ == "__main__":
    print(f"{rotate_matrix('')=}")
