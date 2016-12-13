#! /usr/bin/env python


class Node(object):
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return "[" + ",".join((str(self.getKey()), str(self.getValue()))) + "]"

    def set(self, key, value):
        self.key = key
        self.value = value
    
    def getKey(self):
        return self.key

    def getValue(self):
        return self.value


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __str__(self):
        n = self.head
        content = []
        while n:
            content.append(str(n))
            n = n.next
        return "-->".join(content)

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
        self.insertBefore(node, self.head)

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
        self.count += 1

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
        if node is not None:
            self.remove(node)
        return node

    def removeFirst(self):
        node = self.head
        if node is not None:
            self.remove(node)
        return node

    def search(self, key):
        node = self.head
        while node:
            if node.getItem() == key:
                return node
        return None

    def getAll(self):
        n = self.head
        content = []
        while n:
            content.append(n.getItem())
            n = n.next
        return content


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.slots_available = capacity
        self.cacheLine = DoublyLinkedList()
        self.entries = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = -1
        if key in self.entries:
            cache = self.entries[key]
            self.updateCacheLine(key, cache)
            value = cache.getValue()
        print "GET: key=%d, value=%d, slots=%d" % (key, value,self.slots_available)
        self.status()
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        print "SET: key=%d, value=%d, slots=%d" % (key, value,self.slots_available)
        cache = None
        if key in self.entries:
            cache = self.entries[key]
            cache.setValue(value)
        elif self.slots_available > 0:
            cache = self.createCacheEntry(key, value)
        else:
            cache = self.evict()
            if cache is not None:
                # print "Evicted: %d" % cache.getKey()
                cache.set(key,value)
                self.slots_available -= 1

        if cache is not None:
            self.updateCacheLine(key, cache)
        self.status()

    def createCacheEntry(self, key, value):
        if self.slots_available > 0:
            cache = Node(key, value)
            self.slots_available -= 1
            return cache
        return None

    def updateCacheLine(self, key, cache):
        if key in self.entries:
            self.cacheLine.move2Head(cache)
        else:
            self.entries[key] = cache
            self.cacheLine.insertAsHead(cache)

    def evict(self):
        if self.cacheLine.hasItem():
            cache = self.cacheLine.removeLast()
            key = cache.getKey()
            self.entries.pop(key)
            self.slots_available += 1
            return cache
        return None

    def status(self):
        print self.entries
        print self.cacheLine
        print "-----------------------------\n"
