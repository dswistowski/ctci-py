"""
Implement an algorith to delete a node in the middle, give access only to that node
"""
import pytest
from linked_list import Node, from_iterable


def delete_middle_node(input: Node):
    if not input.next:
        raise RuntimeError("cannot remove last")
    input.data = input.next.data
    input.next = input.next.next


@pytest.fixture(
    params=[
        delete_middle_node,
    ]
)
def function_under_test(request):
    return request.param


@pytest.mark.parametrize(
    "input,node_no,expected",
    [
        ("abcdefg", 3, "abcefg"),
    ],
)
def test_delete_middle_node(input, node_no, expected, function_under_test):
    head = from_iterable(input)
    node = head
    for _ in range(node_no):
        node = node.next

    function_under_test(node)
    assert head == from_iterable(expected)


if __name__ == "__main__":
    print(f"{delete_middle_node('')=}")
