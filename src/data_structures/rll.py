class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    def insert(self, value):
        new = Node(value)

        if self.head is None:
            self.head = new
            self.tail = new
            self.size += 1
            return

        new.next = self.head
        self.head = new
        self.size += 1

    def append(self, value):
        new = Node(value)

        if self.head is None:
            self.head = new
            self.tail = new
            self.size += 1
            return

        self.tail.next = new
        self.tail = new
        self.size += 1

    

    def delete(self, value):
        previous = None
        actual = self.head
        while actual is not None:
            if actual.value == value:
                if previous is None:
                    self.head = actual.next
                    if self.head is None:
                        self.tail = None
                elif actual is self.tail:
                    self.tail = previous
                else:
                    previous.next = actual.next
                self.size -= 1
                return
            previous = actual
            actual = actual.next
        raise ValueError(value)

    def __len__(self):
        return self.size

    def __iter__(self):
        actual = self.head
        while actual is not None:
            yield actual.value
            actual = actual.next