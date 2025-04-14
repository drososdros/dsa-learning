"""
This is a circular queue with max size predefined
"""


class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = self.max_size * [None]
        self.first = -1
        self.last = -1

    def __repr__(self) -> str:
        return "<-" + str(self.items) + "<-"

    @property
    def _next_first(self):
        if self.first == self.max_size - 1:
            return 0
        return self.first + 1

    @property
    def _next_last(self):
        if self.last == self.max_size - 1:
            return 0
        return self.last + 1

    def is_full(self):
        if self._next_last == self.first:
            return True
        return False

    def is_empty(self):
        if self.first == -1:
            return True
        return False

    def add_queue(self, value):
        if self.is_full():
            return "is full"
        if self.first == -1:
            self.first = 0
        self.last = self._next_last
        self.items[self.last] = value

    def dequeue(self):
        if self.is_empty():
            return "is empty"
        elif self.first == self.last:
            item = self.items[self.first]
            self.items[self.first] = None
            self.first = -1
            self.last = -1
            return item
        else:
            item = self.items[self.first]
            self.items[self.first] = None
            self.first = self._next_first
            return item

    def clear(self):
        self.items = self.max_size * [None]
        self.first = -1
        self.last = -1
