import heapq

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        K = len(lists)
        h = [(n.val, n) for n in lists if n is not None]
        heapq.heapify(h)
        head = None
        prev = head

        while h:
            # print "val: %s" %prev.val
            v, node = heapq.heappop(h)
            if node.next is not None:
                heapq.heappush(h, (node.next.val, node.next))
            if prev:
                prev.next = node
                prev = prev.next
            else:
                head = node
                prev = head
        return head

    
def simplify(h):
    l = []
    while h:
        l.append(h.val)
        h = h.next
    return l
        
def test_mergeKLists_Empty():
    merger = Solution()
    assert merger.mergeKLists([]) == None

def test_mergeKLists_singleNode():
    merger = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    lists = [n1,n2]
    h = merger.mergeKLists(lists)
    res = simplify(h)

    assert h is n1
    assert res == [1,2]

#if __name__ == "__main__":
def test_mergeKLists_2():
    merger = Solution()
    nodes_odd = []
    nodes_even = []
    for i in xrange(10):
        if i % 2 == 0:
            nodes_even.append(ListNode(i))
        else:
            nodes_odd.append(ListNode(i))
    for i,n in enumerate(nodes_odd):
        if i+1 < len(nodes_odd):
            n.next = nodes_odd[i+1]
    for i,n in enumerate(nodes_even):
        if i+1 < len(nodes_even):
            n.next = nodes_even[i+1]
    
    print simplify(nodes_odd[0])
    print simplify(nodes_even[0])

    h = merger.mergeKLists([nodes_odd[0],nodes_even[0]])
    res = simplify(h)
    print res
    assert res == [0,1,2,3,4,5,6,7,8,9]

