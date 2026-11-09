class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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

    # SEARCH - BORRADO
    # HACE LO MISMO QUE {20 in linked_list} - no aporta nada este metodo

    def delete(self, value):
        """Removes the first occurrence; ValueError if not present"""
        previous = None
        actual = self.head
        while actual is not None:
            if actual.value == value:
                # si borrar cabeza
                if previous is None:
                    self.head = actual.next
                    # si la cabeza era el unico elemento
                    if self.head is None:
                        self.tail = None
                else:
                    # borrar elemento intermedio
                    previous.next = actual.next
                # si actualizar cola (se evalua siempre porq )
                if actual is self.tail:
                    self.tail = previous
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