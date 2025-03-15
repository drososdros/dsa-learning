from doubly_circular_linked_list import CircularLinkedList, Node
import pytest


def test_empty_ll_should_succeed():
    ll = CircularLinkedList()

    assert ll.head is None
    assert ll.tail is None


def test_ll_append_method_should_succeed():
    ll = CircularLinkedList()
    node = Node(5)
    ll.append(5)
    assert ll.head == node
    assert ll.tail == node
    assert ll.head.next == node
    assert ll.head.prev == node
    assert ll.tail.next == node
    assert ll.tail.prev == node


def test_ll_append_3_items_should_succeed():
    ll = CircularLinkedList()
    node = Node(5)
    node1 = Node(10)
    node2 = Node(3)
    ll.append(5)
    ll.append(10)
    ll.append(3)

    assert len(ll) == 3

    assert ll.head == node
    assert ll.head.next == node1
    assert ll.head.prev == node2

    assert ll.tail == node2
    assert ll.tail.next == node
    assert ll.tail.prev == node1

    next_node = ll.head.next

    assert next_node == node1
    assert next_node.next == node2
    assert next_node.prev == node


def test_ll_item_method_empty_list_should_fail():
    ll = CircularLinkedList()
    assert len(ll) == 0


def test_ll_iter_method_should_succeed():
    ll = CircularLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    correct_list = [1, 2, 3]
    ll_list = []

    for i in ll:
        ll_list.append(i.item)

    assert correct_list == ll_list


def test_ll_len_method_should_succeed():
    ll = CircularLinkedList()
    assert len(ll) == 0


def test_ll_prepend_method_should_succeed():
    ll = CircularLinkedList()
    node = Node(5)
    ll.prepend(5)
    assert ll.head == node
    assert ll.tail == node
    assert ll.head.next == node
    assert ll.head.prev == node
    assert ll.tail.next == node
    assert ll.tail.prev == node


def test_ll_prepend_3_items_should_succeed():
    ll = CircularLinkedList()
    node = Node(5)
    node1 = Node(10)
    node2 = Node(3)
    ll.prepend(3)
    ll.prepend(10)
    ll.prepend(5)

    assert len(ll) == 3
    assert ll.head == node
    assert ll.head.next == node1
    assert ll.head.prev == node2

    assert ll.tail == node2
    assert ll.tail.next == node
    assert ll.tail.prev == node1

    next_node = ll.head.next

    assert next_node == node1
    assert next_node.next == node2
    assert next_node.prev == node


def test_ll_insert_should_succeed():
    ll = CircularLinkedList()
    node = Node(5)
    node1 = Node(10)
    node2 = Node(3)
    ll.prepend(3)
    ll.prepend(5)
    ll.insert(1, 10)

    assert len(ll) == 3
    assert ll.head == node
    assert ll.head.next == node1
    assert ll.head.prev == node2

    assert ll.tail == node2
    assert ll.tail.next == node
    assert ll.tail.prev == node1

    next_node = ll.head.next

    assert next_node == node1
    assert next_node.next == node2
    assert next_node.prev == node


def test_ll_insert_greater_index_raise_IndexError_should_fail():
    ll = CircularLinkedList()
    ll.prepend(3)
    with pytest.raises(IndexError)as e:
        ll.insert(5, 12)
    assert str(e.value) == "Linked list Index out of range"


def test_ll_insert_lower_index_raise_IndexError_should_fail():
    ll = CircularLinkedList()
    ll.prepend(3)
    with pytest.raises(IndexError)as e:
        ll.insert(-1, 12)
    assert str(e.value) == "Linked list Index out of range"


def test_ll_instert_0_intex_should_succeed():
    ll = CircularLinkedList()
    ll.prepend(3)
    node = Node(12)
    ll.insert(0, 12)
    assert ll.head == node


def test_ll_instert_end_intex_should_succeed():
    ll = CircularLinkedList()
    ll.prepend(3)
    ll.prepend(4)
    ll.append(5)
    node = Node(12)
    ll.insert(3, 12)
    assert ll.tail == node


def test_ll_str_method_with_empty_should_succeed():
    ll = CircularLinkedList()
    assert str(ll) == "Empty Linked List"


def test_ll_str_method_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(11)
    assert str(ll) == "5 <-> 10 <-> 11"


def test_ll_get_method_with_empty_list():

    ll = CircularLinkedList()
    n = Node(5)
    assert ll.get(n) is None


def test_ll_get_method_with_positive_out_of_range_should_fail():
    ll = CircularLinkedList()
    ll.append(5)
    with pytest.raises(IndexError) as e:

        ll.get(5)
    assert str(e.value) == "index out of range"


def test_ll_get_method_positive_index_should_succeed():
    ll = CircularLinkedList()
    n = Node(12)
    ll.append(5)
    ll.append(11)
    ll.append(12)
    ll.append(13)
    assert ll.get(2) == n


def test_ll_get_method_with_negative_index_should_succeed():
    ll = CircularLinkedList()
    n = Node(11)
    ll.append(5)
    ll.append(11)
    ll.append(12)
    ll.append(13)
    assert ll.get(-3) == n


def test_ll_get_method_with_negative_index_out_of_range_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    ll.append(11)
    ll.append(12)
    ll.append(13)
    with pytest.raises(IndexError) as e:

        ll.get(-15)
    assert str(e.value) == "index out of range"


def test_ll_get_method_with_node_should_succeed():
    ll = CircularLinkedList()
    n = Node(5)
    ll.append(5)
    found = ll.get(n)
    assert found == n and found is not n


def test_ll_get_method_with_node_dont_exitst_should_fail():
    ll = CircularLinkedList()
    n = Node(12)
    ll.append(5)
    found = ll.get(n)
    assert found is None


def test_ll_pop_method_empty_list_should_fail():
    ll = CircularLinkedList()
    assert ll.pop() is None
    assert ll.head is None
    assert ll.tail is None


def test_ll_pop_method_1_item_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    assert ll.pop().item == 5
    assert ll.length == 0
    assert ll.head is None
    assert ll.tail is None


def test_ll_pop_method_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    ll.append(15)
    ll.append(25)
    ll.append(35)

    assert ll.length == 4
    poped = ll.pop()
    assert poped.next is None
    assert poped.prev is None
    assert poped.item == 35
    assert ll.tail.item == 25
    assert ll.head.prev.item == 25
    assert ll.tail.next.item == 5
    assert ll.length == 3


def test_ll_pop_first_empty_should_fail():
    ll = CircularLinkedList()
    assert ll.pop_first() is None
    assert ll.head is None
    assert ll.tail is None


def test_ll_pop_first_1_item_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    assert ll.length == 1
    poped = ll.pop_first()
    assert poped.next is None
    assert poped.prev is None
    assert poped.item == 5
    assert ll.length == 0
    assert ll.head is None
    assert ll.tail is None


def test_ll_pop_item_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    ll.append(15)
    ll.append(25)
    ll.append(35)
    assert ll.length == 4
    assert ll.pop_first().item == 5
    assert ll.head.item == 15
    assert ll.head.prev.item == 35
    assert ll.tail.next.item == 15
    assert ll.length == 3


def test_ll_clear_should_succeed():
    ll = CircularLinkedList()
    ll.append(5)
    ll.append(15)
    ll.append(25)
    ll.append(35)
    ll.clear()
    assert ll.head is None
    assert ll.tail is None
    assert ll.length == 0
