"""
Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater than or equal to x
"""
import pytest
from linked_list import Node, T, from_iterable


def partition(head: Node[T], element: T) -> Node[T]:
    left = None
    right = None
    current = head
    while current:
        next = current.next
        if current.data < element:
            current.next = left
            left = current
        else:
            current.next = right
            right = current
        current = next

    head = left
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = right
    return head


@pytest.fixture(
    params=[
        partition,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "input, element",
    [
        ([3, 5, 8, 5, 10, 2, 1], 5),
    ],
)
def test_partition(input, element, function_under_test):
    result: Node = function_under_test(from_iterable(input), element)
    left = {e for e in input if e < element}
    right = {e for e in input if not e < element}
    pivot = len(left)
    as_list = result.to_list()
    assert set(as_list[:pivot]) == left
    assert set(as_list[pivot:]) == right


if __name__ == "__main__":
    print(f"{partition(from_iterable([3,5,8,5,10,2,1]), 5)=}")
