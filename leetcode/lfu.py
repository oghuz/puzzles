#! /usr/bin/env python

class Node(object):
    def __init__(self, item=None, prev=None, next=None):
        self.data = item
        self.prev = prev
        self.next = next
    def __str__(self):
        str(data)

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, node):
        if head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        
        self.tail = node
        self.count +=1
    
    def insertBefore(self, node):
        pass

    def remove(self,node):
        if node.prev:
            node.prev.next = node.next
        else:
            head = node.next
            if head:
                head.prev = None
            else:
                head = None
                tail = None
        if node.next:
            node.next.prev = node.prev
        else:
            tail = node.prev 
            tail.next = None

    def search(self, key):
        node = self.head
        while node:
            if node.data ==key:
                return node
        return None



        
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

def test_LFUCache():
    cache = LFUCache(2)
    assert cache.fizzBuzz(1) == ["1"]
    assert cache.fizzBuzz(2) == ["1","2"]
    assert cache.fizzBuzz(3) == ["1","2","Fizz"]
    assert cache.fizzBuzz(4) == ["1","2","Fizz","4"]
    assert cache.fizzBuzz(5) == ["1","2","Fizz","4", "Buzz"]
    assert cache.fizzBuzz(15) == ["1","2","Fizz","4", "Buzz", "Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

if __name__== '__main__':
    cache = LFUCache()
    cache.test_fizzBuzz()
