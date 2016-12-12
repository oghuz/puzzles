#! /usr/bin/env python

from lfu import *


def test_LFUCache_toy():
    cache = LFUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    assert cache.get(1) == 1
    cache.set(3, 3)    # evicts key 2
    assert cache.get(2) == -1    # (not found)
    assert cache.get(3) == 3
    cache.set(4, 4)    # evicts key 1.
    assert cache.get(1) == -1    # (not found)
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_LFUCache_Complex():
    commands = [
        "LFUCache", "set", "set", "set", "set", "set", "get", "set", "get",
        "get", "set", "get", "set", "set", "set", "get", "set", "get", "get",
        "get", "get", "set", "set", "get", "get", "get", "set", "set", "get",
        "set", "get", "set", "get", "get", "get", "set", "set", "set", "get",
        "set", "get", "get", "set", "set", "get", "set", "set", "set", "set",
        "get", "set", "set", "get", "set", "set", "get", "set", "set", "set",
        "set", "set", "get", "set", "set", "get", "set", "get", "get", "get",
        "set", "get", "get", "set", "set", "set", "set", "get", "set", "set",
        "set", "set", "get", "get", "get", "set", "set", "set", "get", "set",
        "set", "set", "get", "set", "set", "set", "get", "get", "get", "set",
        "set", "set", "set", "get", "set", "set", "set", "set", "set", "set",
        "set"
    ]
    params = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13],
              [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5], [1, 30], [11],
              [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10],
              [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4],
              [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27],
              [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29],
              [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26],
              [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9],
              [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13],
              [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17],
              [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1],
              [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
              [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26],
              [13, 28], [11, 26]]
    outputs = [
        None, None, None, None, None, None, -1, None, 19, 17, None, -1, None,
        None, None, -1, None, -1, 5, -1, 12, None, None, 3, 5, 5, None, None,
        1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None,
        None, 18, None, None, None, None, 14, None, None, 18, None, None, 11,
        None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30,
        None, 12, 11, None, None, None, None, 29, None, None, None, None, 17,
        -1, 18, None, None, None, -1, None, None, None, 20, None, None, None,
        29, 18, 18, None, None, None, None, 20, None, None, None, None, None,
        None, None
    ]

    cache = LFUCache(params[0][0])

    for i, cmd in enumerate(commands):
        if commands[i] == "get":
            assert cache.get(params[i][0]) == outputs[i]
        elif commands[i] == "set":
            key = params[i][0]
            value = params[i][1] 
            cache.set(key,value)
        else:
            continue
        # assert cache.check() == True


def same(l1, l2):
    if len(l1) != len(l2):
        return False
    for i, item in enumerate(l1):
        if item != l2[i]:
            return False
    return True


def test_EmptyList():
    temp = DoublyLinkedList()
    assert same(temp.getAll(), []) == True


def test_RemoveSingleNodeList():
    temp = DoublyLinkedList()
    n = Node(99)
    temp.append(n)
    assert same(temp.getAll(), [99]) == True
    assert temp.count == 1
    temp.remove(n)
    assert same(temp.getAll(), []) == True
    assert temp.head is None
    assert temp.tail is None
    assert temp.count == 0


def test_Append():
    temp = DoublyLinkedList()
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    assert same(temp.getAll(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert temp.count == 10


def test_RemoveFromHead():
    temp = DoublyLinkedList()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])

    for i in range(10):
        temp.remove(nodes[i])
        assert same(temp.getAll(), expected[i + 1:]) == True
    assert same(temp.getAll(), []) == True


def test_RemoveFromTail():
    temp = DoublyLinkedList()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])

    for i in range(9, -1, -1):
        temp.remove(nodes[i])
        assert same(temp.getAll(), expected[0:i]) == True
        print "Removed item %d" % i
    assert same(temp.getAll(), []) == True


def test_insertBefore():
    temp = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    temp.append(node1)
    assert same(temp.getAll(), [1]) == True
    temp.insertBefore(node2, node1)
    assert same(temp.getAll(), [2, 1]) == True
    temp.insertBefore(node3, node1)
    assert same(temp.getAll(), [2, 3, 1]) == True


def test_insertAfter():
    temp = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    temp.append(node1)
    assert same(temp.getAll(), [1]) == True
    temp.insertAfter(node2, node1)
    assert same(temp.getAll(), [1, 2]) == True
    temp.insertAfter(node3, node1)
    assert same(temp.getAll(), [1, 3, 2]) == True


def test_move2Head():
    temp = DoublyLinkedList()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])

    for i in range(9, -1, -1):
        temp.move2Head(nodes[i])
        last_item = expected.pop()
        expected.insert(0, last_item)
        assert same(temp.getAll(), expected) == True

def test_insertAsHead():
    temp = DoublyLinkedList()
    expected = range(10)
    expected.reverse()
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
        temp.insertAsHead(nodes[i])
    
    assert same(temp.getAll(), expected) == True

def test_removeLast():
    temp = DoublyLinkedList()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nodes = []
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])

    for i in range(9, -1, -1):
        temp.removeLast()
        last_item = expected.pop()
        assert same(temp.getAll(), expected) == True


def test_hasItem():
    temp = DoublyLinkedList()
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nodes = []
    assert temp.hasItem() == False
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
        assert temp.hasItem() == True

    for i in range(10):
        assert temp.hasItem() == True
        temp.remove(nodes[i])
        assert same(temp.getAll(), expected[i + 1:]) == True

    assert temp.hasItem() == False
