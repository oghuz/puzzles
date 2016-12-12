#! /usr/bin/env python

from lfu import *

def test_LFUCache():
    cache = LFUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    assert cache.get(1) == 1
    cache.set(3, 3)    # evicts key 2
    assert cache.get(2) == -1 # (not found)
    assert cache.get(3) == 3 
    cache.set(4, 4) # evicts key 1.
    assert cache.get(1) == -1 # (not found)
    assert cache.get(3) == 3
    assert cache.get(4) == 4

def same(l1,l2):
    if len (l1) != len(l2):
        return False
    for i, item in enumerate(l1):
        if item != l2[i]:
            return False
    return True

def test_EmptyList():
    temp = DoublyLinkedList()
    assert same(temp.getAll(),[]) == True

def test_RemoveSingleNodeList():
    temp = DoublyLinkedList()
    n = Node(99)
    temp.append(n)
    assert same(temp.getAll(),[99]) == True
    assert temp.count == 1
    temp.remove(n)
    assert same(temp.getAll(),[]) == True
    assert temp.head is None
    assert temp.tail is None
    assert temp.count == 0

def test_Append():
    temp = DoublyLinkedList()
    nodes = [] 
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    assert same(temp.getAll(),[0,1,2,3,4,5,6,7,8,9]) == True
    assert temp.count == 10

def test_RemoveFromHead():
    temp = DoublyLinkedList()
    expected = [0,1,2,3,4,5,6,7,8,9]
    nodes = [] 
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    
    for i in range(10):
        temp.remove(nodes[i])
        assert same(temp.getAll(),expected[i+1:]) == True
    assert same(temp.getAll(),[]) == True

def test_RemoveFromTail():
    temp = DoublyLinkedList()
    expected = [0,1,2,3,4,5,6,7,8,9]
    nodes = [] 
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    
    for i in range(9,-1,-1):
        temp.remove(nodes[i])
        assert same(temp.getAll(),expected[0:i]) == True
        print "Removed item %d" % i 
    assert same(temp.getAll(),[]) == True

def test_insertBefore():
    temp = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    temp.append(node1)
    assert same(temp.getAll(),[1]) == True
    temp.insertBefore(node2,node1)
    assert same(temp.getAll(),[2,1]) == True
    temp.insertBefore(node3,node1)
    assert same(temp.getAll(),[2,3,1]) == True
    
def test_insertAfter():
    temp = DoublyLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    temp.append(node1)
    assert same(temp.getAll(),[1]) == True
    temp.insertAfter(node2,node1)
    assert same(temp.getAll(),[1,2]) == True
    temp.insertAfter(node3,node1)
    assert same(temp.getAll(),[1,3,2]) == True

def test_move2Head():
    temp = DoublyLinkedList()
    expected = [0,1,2,3,4,5,6,7,8,9]
    nodes = [] 
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    
    for i in range(9,-1,-1):
        temp.move2Head(nodes[i])
        last_item = expected.pop()
        expected.insert(0,last_item) 
        assert same(temp.getAll(),expected) == True

def test_removeLast():
    temp = DoublyLinkedList()
    expected = [0,1,2,3,4,5,6,7,8,9]
    nodes = [] 
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    
    for i in range(9,-1,-1):
        temp.removeLast()
        last_item = expected.pop()
        assert same(temp.getAll(),expected) == True

def test_hasItem():
    temp = DoublyLinkedList()
    expected = [0,1,2,3,4,5,6,7,8,9]
    nodes = []
    assert temp.hasItem() ==False
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
        assert temp.hasItem() ==True
    
    for i in range(10):
        assert temp.hasItem() ==True
        temp.remove(nodes[i])
        assert same(temp.getAll(),expected[i+1:]) == True

    assert temp.hasItem() == False
