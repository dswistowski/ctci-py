"""
Write code do remove duplicates from an unsorted linked list
"""
import pytest
import typing as t

from linked_list import Node, from_iterable


T = t.TypeVar("T")


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
