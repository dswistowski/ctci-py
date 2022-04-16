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


def from_iterable(inputs: T) -> Node[T] | None:
    current = None
    for data in reversed(inputs):
        current = Node(next=current, data=data)
    return current
