"""
Rotate matrix by 90 degree
"""
import pytest


def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return matrix
    rows = [False for _ in matrix]
    cols = [False for _ in matrix[0]]
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == 0:
                rows[y] = True
                cols[x] = True

    for x, clear in enumerate(rows):
        if clear:
            for y in range(len(cols)):
                matrix[x][y] = 0
    for y, clear in enumerate(cols):
        if clear:
            for x in range(len(rows)):
                matrix[x][y] = 0
    return matrix


@pytest.fixture(
    params=[
        zero_matrix,
    ]
)
def function_under_test(request):
    return request.param


m1 = [
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6],
]
m1r = m1

m2 = [
    [1, 2, 3],
    [1, 0, 3],
    [1, 2, 3],
]

m2r = [
    [1, 0, 3],
    [0, 0, 0],
    [1, 0, 3],
]

m3 = [[1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1]]

m3r = [[0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1]]


@pytest.mark.parametrize(
    "matrix,result",
    [
        (m1, m1r),
        (m2, m2r),
        (m3, m3r),
    ],
)
def test_zero_matrix(matrix, result, function_under_test):
    assert function_under_test(matrix) == result


if __name__ == "__main__":
    print(f"{zero_matrix(m1)=}")
