"""
Implement an algorithm to find the kth to the last element of singly linked list
"""
import pytest
from linked_list import Node, from_iterable


def return_kth_to_last(input: Node, k: int):
    tail = input
    for _ in range(k + 1):
        try:
            tail = tail.next
        except AttributeError:
            return None

    while tail:
        input = input.next
        tail = tail.next
    return input.data


@pytest.fixture(
    params=[
        return_kth_to_last,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "input,k,expected",
    [
        ("abcd", 0, "d"),
        ("abcd", 1, "c"),
        ("abcd", 2, "b"),
        ("abcd", 3, "a"),
        ("abcd", 4, None),
    ],
)
def test_return_kth_to_last(input, k, expected, function_under_test):
    assert function_under_test(from_iterable(input), k) == expected


if __name__ == "__main__":
    print(f"{return_kth_to_last(from_iterable('abcd'), 2)=}")
