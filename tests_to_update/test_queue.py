import pytest

from data_structures.queue import Queue

def test_queue_vacio():
    q = Queue()
    #assert q.cabeza is None
    assert q.is_empty()   # mejor esto, a traves de la interfaz, no desde las tripas

def test_enqueue_vacio():
    q = Queue()
    q.enqueue(10)
    #assert q.cabeza.valor == 10
    assert q.peek() == 10 # mejor esto

def test_enqueue_no_vacio():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    assert q.dequeue() == 20

def test_dequeue_vacio():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_dequeue_no_vacio():
    q = Queue()
    q.enqueue(10)
    dequeued = q.dequeue()
    assert dequeued == 10

def test_queue_order():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    a = q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    b = q.dequeue()
    c = q.dequeue()
    d = q.dequeue()
    e = q.dequeue()
    numbers = [a,b,c,d,e]
    assert numbers == [10, 20, 30, 40, 50]

def test_queue_reuso_tras_vaciar():
    q = Queue()
    q.enqueue(1)
    q.dequeue()            # queda vacía; aquí cola podría quedar colgando
    q.enqueue(2)
    assert q.dequeue() == 2
    assert q.is_empty()