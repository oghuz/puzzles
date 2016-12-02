#! /usr/bin/env python


def twosum(nums,target):
    index_map = {}
    for i,n in enumerate(nums):
        delta = target - n
        if delta in index_map:
            return [index_map[delta],i]
        index_map[n] = i

def test_twosum():
    assert twosum([2,4],6) == [0,1]
    assert twosum([2,3,4],6) == [0,2]
    assert twosum([4,3,4],8) == [0,2]

if __name__== '__main__':
    test_twosum()

