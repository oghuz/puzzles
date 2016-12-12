#! /usr/bin/env python
import bisect
from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.length = len(words)
        self.freq = defaultdict(list)
        for i,word in enumerate(words):
            self.freq[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.freq[word1]
        l2 = self.freq[word2]
        mindist= self.length
        for i in l1:
            j = bisect.bisect_left(l2, i)
            print j
            if j< len(l2):
                dist = abs(l2[j]-i)
                if dist < mindist:
                    mindist = dist
            if j>0:
                dist = abs(l2[j-1]-i)
                if dist < mindist:
                    mindist = dist
        return mindist


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

def test_dist():
    sol = WordDistance(["a","b"])
    assert sol.shortest("a","b") == 1
    assert sol.shortest("b","a") == 1



