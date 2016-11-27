#! /usr/bin/env python 

from longestCommonSubsequence import * 
import unittest

class LCSTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lcs("",""),[])
    
    def test_self(self):
        x = "ABCDEFG"
        c = lcs(x,x)
        s = getSolution(c,x,x)
        self.assertEqual(s,x)
    
    def test_singleNumber(self):
        x = "ABCBDAB"
        y = "BDCABA"
        c = lcs(x,y)
        s = getSolution(c,x,y)
        self.assertEqual(s,"BCBA")
    
    def test_memoization(self):
        x = "ABCBDAB"
        y = "BDCABA"
        cc = lcs(x,y)
        c = memoized_lcs(x,y)
        for i in xrange(len(x)):
            for j in xrange(len(y)):
                if c[i][j] >0:
                    self.assertEqual(c[i][j],cc[i][j])
        s = getSolution(c,x,y)
        self.assertEqual(s,"BCBA")

if __name__ == '__main__':
    unittest.main()

