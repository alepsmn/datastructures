import pytest
from data_structures.stack import Stack

def test_stack_vacio():
    stack = Stack()
    #assert stack.cabeza is None
    assert stack.is_empty() # mejor esto

def test_stack_push_vacio():
    stack = Stack()
    stack.push(10)
    #assert stack.cabeza.valor == 10
    assert stack.peek() == 10 # mejor esto

def test_stack_push_no_vacio():
    stack = Stack()
    stack.push(10)
    stack.push(20)

    assert stack.cabeza.valor == 20

def test_stack_pop_vacio():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
    # as exc --> assert "vacio" in str(exc.value) SOLO SI LA EXC LLEVA MENSAJE

def test_stack_pop_no_vacio():
    s = Stack()
    s.push(10)
    s.push(20)

    numero = s.pop()
    assert numero == 20

def test_stack_len_peek():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    assert len(s) == 5
    s.pop()
    s.push(60)

    assert len(s) == 5
    empty = s.is_empty()
    assert empty == False
    head = s.peek()
    assert head == 60

def test_stack_order():
    s = Stack()
    s.push(10)
    s.push(20)
    a = s.pop()
    s.push(30)
    s.push(40)
    s.push(50)
    b = s.pop()
    c = s.pop()
    d = s.pop()
    e = s.pop()
    numbers = [a,b,c,d,e]
    assert numbers == [20, 50, 40, 30, 10]
