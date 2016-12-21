import math

class Solution(object):
    def maxProfit(self, prices):
        """
        :type: List[int]
        :rtype: int
        """
        for i,v in enumerate(prices):

        j = len(prices)
        i = 0
        profit = 0 
        while i != j:
            delta = prices[j] - prices[i]


        return profit


def test_simple():
    trader = Solution()
    assert trader.maxProfit([]) == 0 
    stocks = [1,10]
    assert trader.maxProfit(stocks) == 9 

def test_trade():
    trader = Solution()
    stocks = [7,1,5,3,6,4]
    assert trader.maxProfit(stocks) == 5

def test_bearMarket():
    trader = Solution()
    stocks = [9,7,5,3,2,1]
    assert trader.maxProfit(stocks) == 0

def test_bullMarket():
    trader = Solution()
    stocks = [1,2,3,4,5,6,7,8,9,10]
    assert trader.maxProfit(stocks) == 9

