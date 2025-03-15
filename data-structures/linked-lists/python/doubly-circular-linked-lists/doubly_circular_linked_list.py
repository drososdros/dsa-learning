class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next: Node | None = None
        self.prev: Node | None = None

    def __str__(self) -> str:
        return str(self.item)

    def __eq__(self, other) -> bool:
        return self.item == other.item

    def __gt__(self, other) -> bool:
        return self.item > other.item

    def __lt__(self, other) -> bool:
        return self.item < other.item

    def __ge__(self, other) -> bool:
        return self.item >= other.item

    def __le__(self, other) -> bool:
        return self.item <= other.item


class DoublyCircularLinkedList:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def __iter__(self):
        if not self.head:
            return
        node = self.head
        while node.next is not None:

            yield node

            if node.next == self.head:
                break

            node = node.next

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        if self.length == 0:
            return "Empty Linked List"
        linked_list = []
        for i in self:
            linked_list.append(str(i))
        return " <-> ".join(linked_list)

    def _first_item(self, item) -> None:
        new_node = Node(item)
        new_node.next = new_node
        new_node.prev = new_node
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def append(self, item):
        if self.tail is None or self.head is None:
            self._first_item(item)
            return
        new_node = Node(item)
        new_node.prev = self.tail
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node
        self.head.prev = new_node
        self.length += 1

    def prepend(self, item):
        if self.tail is None or self.head is None:
            self._first_item(item)
            return
        new_node = Node(item)
        new_node.next = self.head
        new_node.prev = self.tail
        self.head.prev = new_node
        self.head = new_node
        self.tail.next = new_node
        self.length += 1

    def insert(self, index, item):
        if index < 0 or index > len(self):
            raise IndexError("Linked list Index out of range")
        if index == 0 or len(self) == 0:
            self.prepend(item)
        elif index == len(self):
            self.append(item)
        else:
            new_node = Node(item)
            for ind, node in enumerate(self):
                if ind == index:
                    break
            new_node.next = node
            new_node.prev = node.prev
            new_node.prev.next = new_node
            node.prev = new_node
            self.length += 1

    def get(self, item: Node | int) -> Node | None:
        if isinstance(item, int):
            positive = False if item < 0 else True
            if positive:
                if item >= self.length:
                    raise IndexError("index out of range")
                node = self.head
                for i in range(item):
                    node = node.next
                return node
            else:
                item = abs(item)
                if item > self.length:
                    raise IndexError("index out of range")
                node = self.head
                for i in range(item):
                    node = node.prev
                return node
        elif isinstance(item, Node):
            for i in self:
                if i == item:
                    return i
            else:
                return None

    def pop(self) -> Node | None:
        if self.head is None or self.tail is None:
            return
        elif len(self) == 1:
            poped_node = self.head
            poped_node.next = None
            poped_node.prev = None
            self.head = None
            self.tail = None
        else:

            poped_node = self.tail
            self.tail = poped_node.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            poped_node.next = None
            poped_node.prev = None
        self.length -= 1
        return poped_node

    def pop_first(self) -> Node | None:
        if self.head is None or self.tail is None:
            return
        elif len(self) == 1:

            poped_node = self.pop()
            return poped_node
        else:
            poped_node = self.head
            self.head = poped_node.next
            self.tail.next = self.head
            self.head.prev = self.tail
            poped_node.next = None
            poped_node.prev = None
            self.length -= 1
            return poped_node

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
