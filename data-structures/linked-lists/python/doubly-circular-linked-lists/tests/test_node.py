import pytest
from doubly_circular_linked_list import Node


def test_create_node_should_succeed():
    node = Node(1)
    assert node.next is None
    assert node.prev is None
    assert node.item == 1


def test_create_empty_Node_should_raise_TypeError():
    with pytest.raises(TypeError) as e:
        Node()
    assert "missing 1 required positional argument" in str(e.value)


def test_node_eq_node_should_succeed():
    node1 = Node(2)
    node2 = Node(2)
    assert node1 == node2


def test_node_str_with_number_should_succeed():
    node = Node(5)
    assert "5" == str(node)


def test_node_str_with_string_should_succeed():
    node = Node("Test Str")
    assert "Test Str" == str(node)


def test_node_gt_lt_method_should_succeed():
    """Here i write test for __gt__ and __lt__"""

    node = Node(5)
    node1 = Node(10)
    assert node < node1
    assert (node > node1) is False
    assert node1 > node
    assert (node1 < node) is False


def test_node_gte_lte_method_should_succeed():
    """Here i write test for __gt__ and __lt__"""

    node = Node(5)
    node1 = Node(10)
    node3 = Node(5)
    assert node <= node1
    assert (node >= node1) is False
    assert node1 >= node
    assert (node1 <= node) is False
    assert node3 <= node
    assert node3 >= node
