import pytest
from data_structures.linked_lists import LinkedList

def test_empty_list():
    linked_list = LinkedList()

    assert len(linked_list) == 0
    assert 2 not in linked_list
    # permitido por __iter__
    assert list(linked_list) == [] # itera sobre mis valores -> lista

    with pytest.raises(ValueError):
        linked_list.delete(2)

def test_append_insert_order():
    linked_list = LinkedList()

    for i in range(4):
        linked_list.append(i*10)
    assert list(linked_list) == [0, 10, 20 ,30]
    assert len(linked_list) == 4

    for i in range(4):
        linked_list.insert(i*10)
    assert list(linked_list) == [30, 20, 10, 0, 0, 10, 20, 30]
    assert len(linked_list) == 8


def test_delete_first_duplicate():
    linked_list = LinkedList()
    for i in range(4):
        linked_list.append(i*10)

    linked_list.append(10)
    assert list(linked_list) == [0, 10, 20 ,30, 10]
    linked_list.delete(10)
    assert list(linked_list) == [0, 20 ,30, 10]
    
def test_delete_middle():
    linked_list = LinkedList()
    for i in range(4):
        linked_list.append(i*10)

    linked_list.delete(20)
    assert list(linked_list) == [0, 10, 30]
    assert len(linked_list) == 3

def test_delete_tail_state():
    '''Un assert que no mira justo después del cambio no verifica el cambio.'''
    linked_list = LinkedList()
    for i in [0, 10, 20, 30]:
        linked_list.append(i)

    linked_list.delete(30)
    assert list(linked_list) == [0, 10, 20]
    assert len(linked_list) == 3
    assert linked_list.tail.value == 20

def test_delete_ends():
    linked_list = LinkedList()
    for i in range(4):
        linked_list.append(i*10)

    linked_list.delete(0)
    linked_list.delete(30)
    linked_list.append(25)

    assert list(linked_list) == [10, 20, 25]
    assert len(linked_list) == 3

def test_delete_unique():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.delete(10)
    assert list(linked_list) == []
    assert len(linked_list) == 0

    linked_list.append(20)
    assert list(linked_list) == [20]

def test_delete_not_present():
    linked_list = LinkedList()
    linked_list.append(10)

    with pytest.raises(ValueError):
        linked_list.delete(20)

    assert list(linked_list) == [10]
    assert len(linked_list) == 1