# Best Time to Buy and Sell Stock II (122)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            if (prices[i+1] - prices[i]) > 0:
                profit += ( prices[i+1] - prices[i] )
        
        return profit


print(Solution().maxProfit( prices = [7,1,5,3,6,4]))
print(Solution().maxProfit( prices = [1,2,3,4,5]))
print(Solution().maxProfit( prices = [7,6,4,3,1]))
print(Solution().maxProfit( prices = [2,4,1]))

"""
[7,1,5,3,6,4]
    4  0  3 =  7
[1,2,3,4,5]
0 1 1 1 1 = 5

[2, 4, 1]
0 2  0 = 2
"""