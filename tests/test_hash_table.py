import pytest

from data_structures.hash_table import CARGA_MAXIMA, HashTable


def test_empty_hash_table():
    hash_t = HashTable()

    assert len(hash_t) == 0

    with pytest.raises(KeyError):
        hash_t.get("ab")

    assert ("ab" in hash_t) == False

def test_internal_integrity():
    hash_t = HashTable()

    hash_t.put("ab", 10)
    assert hash_t.get("ab") == 10

    hash_t.put("ab", 20)
    assert hash_t.get("ab") == 20
    assert len(hash_t) == 1

    # Test collision
    hash_t.put("cd", 30)
    assert hash_t.get("ab") == 20
    assert hash_t.get("cd") == 30
    assert len(hash_t) == 2

def test_resize():
    hash_t = HashTable()
    for i in range(20):
        hash_t.put(f'f{i}', i)

    assert len(hash_t) == 20

    for i in range(20):
        assert hash_t.get(f'f{i}') == i

def test_internal_resize():
    hash_t = HashTable()
    for i in range(20):
        hash_t.put(f'f{i}', i)
    assert len(hash_t)/len(hash_t.buckets) <= CARGA_MAXIMA
    assert len(hash_t.buckets) > 8

def test_delete():
    hash_t = HashTable()
    hash_t.put("ab", 10)
    hash_t.put("xz", 20)

    assert len(hash_t) == 2

    hash_t.delete("xz")
    assert len(hash_t) == 1
    assert "xz" not in hash_t

    with pytest.raises(KeyError):
        hash_t.get("xz")

    with pytest.raises(KeyError):
        hash_t.delete("xz")

    assert len(hash_t) == 1