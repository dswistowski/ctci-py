"""
Write cote do remove duplicates from an unsorted linked list
"""
from dataclasses import dataclass
import typing as t

import pytest

T = t.TypeVar("T")


@dataclass(eq=False)
class Node(t.Generic[T]):
    next: t.Optional["Node"]
    data: T

    def to_list(self) -> list[T]:
        if not self.next:
            return [self.data]
        return [self.data, *self.next.to_list()]

    def __eq__(self, other) -> bool:
        if self.__class__ == other.__class__:
            return self.to_list() == other.to_list()
        return False


def from_iterable(inputs: T) -> Node[T] | None:
    current = None
    for data in reversed(inputs):
        current = Node(next=current, data=data)
    return current


def remove_dups(input: Node[T]) -> Node[T]:
    start = input
    current = start
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return input


def remove_dups_with_memory(input: Node[T]) -> Node[T]:
    exists = set()
    current = input
    previous = None
    while current:
        if current.data in exists:
            previous.next = current.next
        else:
            exists.add(current.data)
            previous = current
        current = current.next

    return input


@pytest.fixture(params=[remove_dups, remove_dups_with_memory])
def function_under_test(request):
    return request.param


def test_from_iterable():
    assert from_iterable("abcd") == Node(
        data="a",
        next=Node(data="b", next=Node(data="c", next=Node(data="d", next=None))),
    )


@pytest.mark.parametrize(
    "input,expected",
    [
        ("abc", "abc"),
        ("abbc", "abc"),
        ("abbbc", "abc"),
        ("abca", "abc"),
        ("bbbbbbbbb", "b"),
        ("", ""),
        ("aaabbb", "ab"),
    ],
)
def test_remove_dups(input, expected, function_under_test):
    assert function_under_test(from_iterable(input)) == from_iterable(expected)


if __name__ == "__main__":
    print(f"{remove_dups(from_iterable('abcda'))=}")
