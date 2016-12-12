#! /usr/bin/env python
from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.counter = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.counter:
            self.counter[number] = 2
        else:
            self.counter[number] = 1
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        d = self.counter
        for n in d.keys():
            delta = value - n
            if delta in d:
                if delta != n:
                    return True
                elif d[n] > 1:
                    return True
        return False
        
def test_TwoSum():
    sol = TwoSum()
    #for i in [0,0,0,-1,0,1,1,0]:
    sol.add(0)
    sol.add(0)
    assert sol.find(0)== True
    sol.add(0)
    sol.add(-1)
    sol.add(0)
    sol.add(1)
    assert sol.find(0)== True
    sol.add(1)
    assert sol.find(1)== True
    assert sol.find(2)== True
    assert sol.find(3)== False



