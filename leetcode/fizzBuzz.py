#! /usr/bin/env python

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [] 
        for i in xrange(1,n+1):
            info = str(i) 
            mul_three = (i % 3 == 0)
            mul_five = (i % 5 == 0)
            if mul_three:
                info = "Fizz"
            if mul_five:
                info = "Buzz"
            if mul_three and mul_five:
                info = "FizzBuzz"
            res.append(info)
        return res

def test_fizzBuzz():
    sol = Solution()
    assert sol.fizzBuzz(1) == ["1"]
    assert sol.fizzBuzz(2) == ["1","2"]
    assert sol.fizzBuzz(3) == ["1","2","Fizz"]
    assert sol.fizzBuzz(4) == ["1","2","Fizz","4"]
    assert sol.fizzBuzz(5) == ["1","2","Fizz","4", "Buzz"]
    assert sol.fizzBuzz(15) == ["1","2","Fizz","4", "Buzz", "Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

if __name__== '__main__':
    sol = Solution()
    sol.test_fizzBuzz()

