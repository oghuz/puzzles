import math

class Solution(object):
    def getFactors(self, n, base=2):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        factorization = []
        for i in xrange(base,int(math.sqrt(n))+1):
            if n % i ==0:
                j = n/i
                factorization.append([i,j])
                factors = self.getFactors(j,i)
                for factor in factors:
                    combo = [i] + factor
                    factorization.append(combo)
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
    assert same(factor.getFactors(1), []) == True
    assert same(factor.getFactors(37), []) == True
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
