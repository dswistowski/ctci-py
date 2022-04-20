"""
Design stack which in addition to push and pop has a function min. Push pop and min should operate in O(1) time
"""
import dataclasses as dt
import typing as t

import pytest

T = t.TypeVar("T")

"""
 5 
 4
 7
 3
 6
"""


@dt.dataclass
class Node(t.Generic[T]):
    value: T
    next: t.Optional["Node"] = None
    smaller: t.Optional["Node"] = None


class StackMin(t.Generic[T]):
    head: Node | None
    _min: Node | None

    def __init__(self):
        self.head = None
        self._min = None

    def push(self, value: T) -> None:
        if self.head is None:
            self.head = Node(value=value)
            self._min = self.head
        else:
            self.head = Node(value=value, next=self.head)
            if value < self._min.value:
                self._min.smaller = self.head
                self._min = self.head

    def pop(self) -> T:
        if self.head is None:
            raise RuntimeError("stack is empty")
        if id(self._min) == id(self.head):
            self._min = self.head.next
        current = self.head
        self.head = self.head.next
        return current.value

    def min(self) -> T:
        if self._min is None:
            raise RuntimeError("stack is empty")
        return self._min.value


@pytest.fixture(
    params=[
        StackMin,
    ]
)
def StackImplementation(request):
    return request.param


def test_stack_min(StackImplementation):
    s = StackImplementation()
    s.push(5)
    assert s.min() == 5
    s.push(3)
    assert s.min() == 3
    assert s.pop() == 3
    assert s.min() == 5
    s.push(3)
    s.push(6)
    s.push(2)
    s.push(7)
    assert s.min() == 2
    assert s.pop() == 7
    assert s.min() == 2
