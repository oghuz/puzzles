#! /usr/bin/env python

from lru import *


def test_LRUCache_toy():
    cache = LRUCache(2)
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


