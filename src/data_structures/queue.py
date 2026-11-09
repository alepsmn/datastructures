class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Queue:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def enqueue(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            self.tamano += 1
            return

        self.cola.siguiente = nuevo
        self.cola = nuevo
        self.tamano += 1

    def dequeue(self):
        if self.cabeza is None:
            raise IndexError

        dequeued = self.cabeza
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        self.tamano -= 1
        return dequeued.valor

    def peek(self):
        if self.cabeza is None:
            raise IndexError
        return self.cabeza.valor
    
    def __len__(self):
        return self.tamano

    def is_empty(self):
        return self.tamano == 0
