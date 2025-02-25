# 123. Best Time to Buy and Sell Stock III
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        profit = 0
        profits = []

        for i in range(1, len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                profits.append(prices[i + 1] - prices[i])
        
        profits = sorted(profits)[::-1]
        profit = sum(profits[:2])
        return profit
    

print(Solution().maxProfit(prices = [3,3,5,0,0,3,1,4]))
print(Solution().maxProfit(prices = [1,2,3,4,5]))