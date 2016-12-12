#! /usr/bin/env python


class Node(object):
    def __init__(self, item=None, prev=None, next=None):
        self.data = item
        self.prev = prev
        self.next = next

    def __str__(self):
        str(self.data)

    def getItem(self):
        return self.data

    def setItem(self,item):
        self.data = item 


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def hasItem(self):
        return self.count > 0

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.count += 1

    def move2Head(self, node):
        if node is self.head:
            return

        self.remove(node)
        self.insertBefore(node, self.head)
    
    def insertAsHead(self, node):
        self.insertBefore(node,self.head)

    def insertBefore(self, node, pos):
        if pos is None:
            self.append(node)
            return
        pred = pos.prev
        if pred is None:
            self.head = node
        else:
            pred.next = node

        node.prev = pred
        node.next = pos
        pos.prev = node
        self.count +=1

    def insertAfter(self, node, pos):
        if pos is None:
            self.append(node)
            return
        succ = pos.next
        if succ is None:
            self.tail = node
        else:
            succ.prev = node

        node.next = succ
        pos.next = node
        node.prev = pos
        self.count += 1

    def remove(self, node):
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
        self.count -= 1

    def removeLast(self):
        node = self.tail
        self.remove(node)
        return node
        
    
    def getHead(self):
        return self.head

    def search(self, key):
        node = self.head
        while node:
            if node.val == key:
                return node
        return None

    def getAll(self):
        n = self.head
        content = []
        while n:
            content.append(n.getItem())
            n = n.next
        return content


class CacheEntry(object):
    Value = 0
    Frequency = 1
    Structure = 2


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.slots_available = capacity
        self.capacity = capacity
        self.entries = {}
        self.freqList = DoublyLinkedList()
        # n = Node(0)
        # self.freqList.append(n)
        self.freqListDictionary = {}
        self.freqGroup= {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.entries:
            cache = self.entries[key][CacheEntry.Structure]
            self.increaseReferenceCount(key,cache)
            return self.entries[key][CacheEntry.Value]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.entries:
            self.entries[key][CacheEntry.Value] = value
        elif self.slots_available > 0:
            self.createCacheEntry(key,value)
        else:
            self.evict()
            self.createCacheEntry(key,value)
        
        cache = self.entries[key][CacheEntry.Structure]
        self.increaseReferenceCount(key,cache)


    def createCacheEntry(self, key,value):
        if self.slots_available >0:
            self.entries[key] = [value, 0, Node(key)]
            self.slots_available -= 1
            return True
        return False

    def increaseReferenceCount(self, key, cache):
        refCount = self.entries[key][CacheEntry.Frequency]
        new_refCount = refCount + 1
        if new_refCount not in self.freqListDictionary:
            itemList = DoublyLinkedList()
            n = Node(item = itemList)
            self.freqListDictionary[new_refCount] = n
            if refCount>0:
                pos = self.freqListDictionary[refCount] 
                self.freqList.insertAfter(n,pos)
            else:
                self.freqList.insertAsHead(n)

        if refCount >0:
            node = self.freqListDictionary[refCount]
            q1 = node.getItem()
            q1.remove(cache)
            if not q1.hasItem():
                self.freqList.remove(node)

        q2 = self.freqListDictionary[new_refCount].getItem()
        q2.insertAsHead(cache)
        self.entries[key][CacheEntry.Frequency] += 1

    def evict(self):
        lfu_queue = self.freqList.getHead().getItem()
        key = lfu_queue.removeLast().getItem()
        self.entries.pop(key)
        self.slots_available +=1

