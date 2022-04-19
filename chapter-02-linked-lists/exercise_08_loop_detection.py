"""
Given a linked list which might contain a loop, implement and algorithm that returns the node at the begining of the loop
"""
import pytest

from linked_list import Node, from_iterable


def loop_detection_memory(head: Node):
    visited = set()
    while head:
        if id(head) not in visited:
            visited.add(id(head))
        else:
            return head
        head = head.next
    return None


def loop_detection_tortioise_and_hare(head: Node):
    """
    Floyd's tortoise and hare
    hare    : abcd efgh efgh e
    tortoise: bdfh fhfh abcd e
    """
    hare = head
    tortoise = head.next
    while tortoise and tortoise.next and id(tortoise) != id(hare):
        hare = hare.next
        tortoise = tortoise.next.next
    if id(tortoise) == id(hare):
        hare = hare.next
        tortoise = head
        while id(tortoise) != id(hare):
            hare = hare.next
            tortoise = tortoise.next
        return hare
    else:
        return None


@pytest.fixture(params=[loop_detection_memory, loop_detection_tortioise_and_hare])
def function_under_test(request):
    return request.param


def make_loop(head: Node, loop: Node | None):
    current = head
    if loop:
        for _ in range(loop):
            current = current.next
        loop = current
        while current.next:
            current = current.next
        current.next = loop
    return head, loop


@pytest.mark.parametrize(
    "head,loop",
    [
        (make_loop(from_iterable("abcdefgh"), 4)),
        (make_loop(from_iterable("abcdefgh"), None)),
        (make_loop(from_iterable("abc"), 1)),
    ],
)
def test_loop_detection(head: Node, loop: int, function_under_test):
    assert id(function_under_test(head)) == id(loop)


if __name__ == "__main__":
    head = from_iterable("abcdefgh")

    print(f"{loop_detection_memory(head)=}")
