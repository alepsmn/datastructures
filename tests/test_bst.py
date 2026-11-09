from data_structures.binary_tree import BinaryTree

BALANCED = [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]
UNBALANCED = [7, 3, 9, 5, 8]

def test_arbol_vacio():
    tree = BinaryTree()
    assert tree.search(50) == False

def test_insert_tree():
    tree = BinaryTree()

    tree.insert(50)
    tree.insert(40)
    assert tree.search(40)
    assert 40 in tree
    assert tree.search(50)
    assert 50 in tree

    assert not tree.search(100)
    assert 100 not in tree

def test_duplicates():
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(60)
    tree.insert(50)
    assert tree.search(50)

#----------------------------------------------------------------
def _inorder(tree):
    out = []
    def walk(n):
        if n is None:
            return
        walk(n.left)
        out.append(n.value)
        walk(n.right)
    walk(tree.root)
    return out

def test_delete_leaf():
    bst = BinaryTree()
    for i in BALANCED:
        bst.insert(i)

    bst.delete(14)
    assert not bst.search(14)
    assert _inorder(bst) == sorted(set(BALANCED) - {14})

def test_delete_two_child():
    bst = BinaryTree()
    for i in BALANCED:
        bst.insert(i)

    bst.delete(13)
    assert not bst.search(13)
    assert _inorder(bst) == sorted(set(BALANCED) - {13})

def test_delete_one_child():
    bst = BinaryTree()
    for i in UNBALANCED:
        bst.insert(i)

    bst.delete(3)
    assert not bst.search(3)
    assert _inorder(bst) == sorted(set(UNBALANCED) - {3})

    bst.delete(9)
    assert not bst.search(9)
    assert _inorder(bst) == sorted(set(UNBALANCED) - {3, 9})

def test_delete_root():
    bst = BinaryTree()
    for i in BALANCED:
        bst.insert(i)

    bst.delete(7)
    assert not bst.search(7)
    assert _inorder(bst) == sorted(set(BALANCED) - {7})

def test_back_to_empty():
    bst = BinaryTree()
    bst.insert(1)
    bst.delete(1)
    assert not bst.search(1)
    assert bst.root is None

def test_delete_absent():
    bst = BinaryTree()
    valores = [7, 3, 11, 1, 5]
    for v in valores:
        bst.insert(v)

    bst.delete(99)                      # 99 no está
    assert _inorder(bst) == sorted(set(valores))
    assert not bst.search(99)           # y 99 sigue sin estar