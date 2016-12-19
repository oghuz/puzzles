import bisect
from collections import defaultdict

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        freq = defaultdict(list)
        for i,word in enumerate(words):
            freq[word].append(i)
        mindist = len(words)
        
        l1 = freq[word1]
        if word1 == word2:
            for i,v in enumerate(l1[:-1]):
                mindist = min(abs(v - l1[i+1]), mindist)
            return mindist

        l2 = freq[word2]
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

def test_dist():
    words = ["practice", "makes", "perfect", "coding", "makes"]
    sol = Solution()
    assert sol.shortestWordDistance(words, "makes","coding") == 1
    assert sol.shortestWordDistance(words, "makes","makes") == 3
