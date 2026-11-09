from data_structures.double_linked import DoubleLinked

def test_lista_vacia():
    lista = DoubleLinked()
    assert lista.cabeza is None
    assert lista.cola is None

def test_insert_vacio():
    lista = DoubleLinked()
    lista.insert(10)

    assert lista.cabeza is lista.cola

def test_insert():
    lista = DoubleLinked()
    lista.insert(20)
    lista.insert(10)
    lista.insert(5)

    # forward
    valores = []
    actual = lista.cabeza
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.siguiente

    assert valores == [5, 10, 20]

    #backward
    valores = []
    actual = lista.cola
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.anterior
    assert valores == [20, 10, 5]

    assert lista.cabeza.anterior is None
    assert lista.cola.siguiente is None

def test_delete_unique():
    lista = DoubleLinked()
    nodo = lista.insert(10)
    lista.delete(nodo)

    assert lista.cabeza is None
    assert lista.cola is None

def test_delete_cabeza():
    lista = DoubleLinked()
    lista.insert(20)
    lista.insert(10)
    nodo = lista.insert(5)

    lista.delete(nodo)

    # forward
    valores = []
    actual = lista.cabeza
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.siguiente

    assert valores == [10, 20]

    #backward
    valores = []
    actual = lista.cola
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.anterior
    assert valores == [20, 10]

    assert lista.cabeza.anterior is None
    assert lista.cola.siguiente is None

def test_delete_cola():
    lista = DoubleLinked()
    nodo = lista.insert(20)
    lista.insert(10)
    lista.insert(5)
    lista.delete(nodo)
    # forward
    valores = []
    actual = lista.cabeza
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.siguiente

    assert valores == [5, 10]

    #backward
    valores = []
    actual = lista.cola
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.anterior
    assert valores == [10, 5]

    assert lista.cabeza.anterior is None
    assert lista.cola.siguiente is None

def test_delete_mid():
    lista = DoubleLinked()
    lista.insert(20)
    nodo = lista.insert(10)
    lista.insert(5)

    lista.delete(nodo)
    # forward
    valores = []
    actual = lista.cabeza
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.siguiente

    assert valores == [5, 20]

    #backward
    valores = []
    actual = lista.cola
    while actual is not None:
        valores.append(actual.valor)
        actual = actual.anterior
    assert valores == [20, 5]

    assert lista.cabeza.anterior is None
    assert lista.cola.siguiente is None