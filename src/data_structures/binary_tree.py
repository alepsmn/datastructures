class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node # value left = rigth

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False

        if value < node.value:
            return self._search(node.left, value)
        elif value > node.value:
            return self._search(node.right, value)

        return True

    def __contains__(self, value):
        return self.search(value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:
            # en este punto, ya estas en el nodo que quieres eliminar
            if node.left is None and node.right is None:
                return None

            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right

            successor = self._min_value_node(node.right)
            node.value = successor.value
            # dentro del subarbol derecho, buscamos eliminar el valor del sucesor
            # ya estamos debajo de el -> no hay peligro
            node.right = self._delete(node.right, successor.value)
            # como el nodo que se busca es el minimo de la izquierda, nunca podra
            # tener dos hijos, tendra o hijo a la derecha o ninguno -> tiene fin

        # se ejecuta al final de cada llamada recursiva
        return node

    # dentro del sub arbol derecho del nodo, buscas por su sub sub arbol  izquierdo
    # hasta q no haya mas -> min
    def _min_value_node(self, node):
        if node.left is None:
            return node

        return self._min_value_node(node.left)