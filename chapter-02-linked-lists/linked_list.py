from dataclasses import dataclass
import typing as t

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

    def __repr__(self):
        return f"<Node {self.to_list()}>"


def from_iterable(inputs: T) -> Node[T] | None:
    current = None
    for data in reversed(inputs):
        current = Node(next=current, data=data)
    return current


def push(head: Node, value: T) -> Node:
    return Node(data=value, next=head)


def pop(head: Node) -> tuple[Node, T]:
    return head.next, head.data


def glue(l1: Node, l2: Node | None) -> Node:
    head = l1
    while head.next:
        head = head.next
    head.next = l2
    return l1


def to_stack(list: Node):
    stack = None
    while list:
        stack = push(stack, list)
        list = list.next
    return stack
