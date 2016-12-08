#! /usr/bin/env python

class Node(object):
    def __init__(self, item=None, prev=None, next=None):
        self.val = item
        self.prev = prev
        self.next = next
    def __str__(self):
        str(val)

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        
        self.tail = node
        self.count +=1
    
    def insertBefore(self, node, pos):
        pred = pos.prev
        if pred is None:
            self.head =node
        else:
            pred.next = node

        node.prev = pred
        node.next = pos
        pos.prev = node

    
    def insertAfter(self, node, pos):
        succ = pos.next
        if succ is None:
            self.tail = node
        else:
            succ.prev = node

        node.next = succ
        pos.next = node 
        node.prev = pos

    def remove(self,node):
        pred = node.prev
        succ = node.next 
        if pred is None:
            self.head = succ
        else:
            pred.next = succ
            node.prev = None

        if succ is None:
            if pred:
                pred.next = None
            self.tail = pred
        else:
            succ.prev = pred
            node.next = None
        self.count -=1


    def search(self, key):
        node = self.head
        while node:
            if node.val ==key:
                return node
        return None
    
    def getAll(self):
        n = self.head
        content = []
        while n:
            content.append(n.val)
            n = n.next
        return content



        
class LFUCache(object):
    def __init__(self, capacity):
        """
        
        :type capacity: int
        """
        self.capacity = capacity
        self.tree = BinaryHeap()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
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
        print "Removed item %d" % i 
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


if __name__== '__main__':
    temp = DoublyLinkedList()
    nodes = [] 
    for i in range(10):
        nodes.append(Node(i))
        temp.append(nodes[i])
    temp.remove(nodes[0])
