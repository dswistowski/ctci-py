"""
You have two numbers represented by a linked list, where each node contains a single digit.
The digit are stored in reverse order. Write a function that adds the two numbers and returns the sum as a linked list
"""
import random

import pytest

from linked_list import Node, from_iterable


def sum_lists(l1: Node[int], l2: Node[int]):
    head = None
    current = None
    carry = 0
    while l1 or l2:
        value = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carry
        value, carry = value % 10, value // 10
        new = Node(data=value, next=None)

        if current:
            current.next = new
            current = current.next
        else:
            current = new
            head = new

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry:
        new = Node(data=carry, next=None)
        current.next = new
    return head


@pytest.fixture(
    params=[
        sum_lists,
    ]
)
def function_under_test(request):
    return request.param


def to_list_int(number: int) -> list[int]:
    return [int(d) for d in reversed(str(number))]


# just want to have stable tests
r = random.Random(42)


@pytest.mark.parametrize(
    "l1,l2",
    [(617, 295), *[(r.randint(0, 100000), r.randint(0, 100000)) for _ in range(100)]],
)
def test_sum_lists(l1, l2, function_under_test):
    expected = l1 + l2

    assert function_under_test(
        from_iterable(to_list_int(l1)), from_iterable(to_list_int(l2))
    ) == from_iterable(to_list_int(expected))


if __name__ == "__main__":
    print(
        f"{sum_lists(from_iterable(reversed('617')),from_iterable(reversed('295')) )=}"
    )
