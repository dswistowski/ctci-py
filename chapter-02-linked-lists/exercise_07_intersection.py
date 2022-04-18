"""
Given two linked lists, determine if the two lists intersects. Return the intersecting node
"""
import typing as t

import pytest
from linked_list import Node, from_iterable, pop, glue, to_stack


def intersection_stack(l1: Node, l2: Node) -> Node | None:
    """
    reverse linked lists with stack, and pop as long they pointing to the same node
    """
    inter = None
    s1 = to_stack(l1)
    s2 = to_stack(l2)
    while s1 and s2:
        (s1, l1), (s2, l2) = pop(s1), pop(s2)
        if id(l1.data) != id(l2.data):
            break
        inter = l1
    return inter


def list_len(head: Node) -> int:
    c = 0
    while head:
        head = head.next
        c += 1
    return c


def intersection_normalize(l1: Node, l2: Node) -> Node | None:
    """Make two list the same size, and then pop front to intersection"""
    n1 = list_len(l1)
    n2 = list_len(l2)
    if n1 < n2:
        n1, n2 = n2, n1
        l1, l2 = l2, l1
    while n1 > n2:
        n1 = -1
        l1 = l1.next

    while l1:
        if id(l1) == id(l2):
            return l1
        l1 = l1.next
        l2 = l2.next
    return None


def build(l1: Node, l2: Node, l3: Node | None) -> tuple[Node, Node, Node | None]:
    return glue(l1, l3), glue(l2, l3), l3


@pytest.fixture(params=[intersection_stack, intersection_normalize])
def function_under_test(request):
    return request.param


T = t.TypeVar("T")
K = t.TypeVar("K")


def opt_map(f: t.Callable[[T], K], value: T | None) -> K | None:
    if value is not None:
        return f(value)
    return None


@pytest.mark.parametrize(
    "l1,l2,l3",
    [("abc", "de", "fg"), ("abc", "edf", None)],
)
def test_intersection(l1: str, l2: str, l3: str | None, function_under_test):
    l1, l2, inter = build(
        from_iterable(l1), from_iterable(l2), opt_map(from_iterable, l3)
    )
    assert function_under_test(l1, l2) == inter


if __name__ == "__main__":
    l1, l2 = build(from_iterable("abc"), from_iterable("de"), from_iterable("fg"))
    print(f"{intersection_stack(l1, l2)=}")
