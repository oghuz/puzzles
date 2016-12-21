import math

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type: List[int]
        :rtype: int
        """
        maxAll = nums[0]
        for i in nums:

        return maxAll


def test_simple():
    trader = Solution()
    assert trader.maxProfit([]) == 0 
    stocks = [1,10]
    assert trader.maxProfit(stocks) == 9 

def test_trade():
    trader = Solution()
    stocks = [7,1,5,3,6,4]
    assert trader.maxProfit(stocks) == 5

def test_bullMarket():
    trader = Solution()
    stocks = [-2,1,-3,4,-1,2,1,-5,4]
    assert trader.maxProfit(stocks) == 6

