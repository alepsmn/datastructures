class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        new = Node(value)

        if self.head is None:
            self.head = new
            self.tail = new
            return

        new.next = self.head
        self.head.previous = new
        self.head = new

    def delete(self, node: Node):
        if node is None:
            return

        if node.previous is None:
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous

        node.previous = None
        node.next = None