"""
Implement a function to chekc if a linked list is a palindrome.
"""
import pytest
from linked_list import Node, from_iterable, push, pop


def palindrome(head: Node):
    stack = None
    current = head
    while current:
        stack = push(stack, current)
        current = current.next

    current = head
    while current:
        stack, tail = pop(stack)
        if current.data != tail.data:
            return False
        current = current.next
    return True


@pytest.fixture(
    params=[
        palindrome,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "head,expected",
    [
        (from_iterable("foo"), False),
        (from_iterable(""), True),
        (from_iterable("abba"), True),
        (from_iterable("abcba"), True),
        (from_iterable("abcbaa"), False),
        (from_iterable("saippuakivikauppias"), True),
    ],
)
def test_palindrome(head, expected, function_under_test):
    assert function_under_test(head) == expected


if __name__ == "__main__":
    print(f"{palindrome(from_iterable('saippuakivikauppias'))=}")
