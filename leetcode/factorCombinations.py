
class Solution(object):
    def getFactors(self, n, usedFactors=None):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if usedFactors is None:
            usedFactors = set()
        factorization = []
        for i in xrange(2,n):
            if n % i ==0:
                j = n/i
                if j not in usedFactors:
                    factorization.append([i,j])
                    factors = self.getFactors(j,usedFactors)
                    for factor in factors:
                        combo = [i] + factor
                        factorization.append(combo)
                    usedFactors.add(i)
                    usedFactors.add(j)

        return factorization


def same(l1, l2):
    if len(l1) != len(l2):
        return False
    for i, item in enumerate(l1):
        if item != l2[i]:
            return False
    return True
 
def test_Factors():
    factor = Solution()
    assert len(factor.getFactors(1)) == 0
    assert len(factor.getFactors(37)) == 0
    expected = [[2, 6],[2, 2, 3],[3, 4]]
    calculated = factor.getFactors(12)
    for i,factorization in enumerate(expected):
         assert same(calculated[i],factorization) ==True

if __name__=='__main__':
    import sys
    if len(sys.argv) ==1:
        print "Missing argument. [n] the number to factorize"
        exit(1)
    n = int(sys.argv[1]) 
    sol = Solution()
    print sol.getFactors(n)
