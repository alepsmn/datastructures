class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new = Node(value)
        self.size += 1

        if self.head is None:
            self.head = new
            return

        new.next = self.head
        self.head = new

    def pop(self):
        if self.head is None:
            raise IndexError

        self.size -= 1
        popped = self.head
        self.head = self.head.next
        return popped.value

    def peek(self):
        if self.head is None:
            raise IndexError

        return self.head.value

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0