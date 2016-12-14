class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = {}
        vio = set()
        for i,c in enumerate(s):
            if c in mapping:
                if t[i] != mapping[c]:
                    return False
            elif t[i] not in vio:
                mapping[c] = t[i]
                vio.add(t[i])
            else:
                return False
        return True


def test_IsomorphicStrings():
    iso = Solution()
    assert iso.isIsomorphic("ab","aa") == False
    assert iso.isIsomorphic("egg","add") == True
    assert iso.isIsomorphic("foo","bar") == False
    assert iso.isIsomorphic("paper","title") == True

#iso = Solution()
#print iso.isIsomorphic("paper","title")

