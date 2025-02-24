from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        index = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
                index = i
            
        
            profit = max(profit, max(prices[index:]) - minimum)

        return profit



print(Solution().maxProfit( prices = [7,1,5,3,6,4]))
print(Solution().maxProfit( prices = [7,6,4,3,1]))
print(Solution().maxProfit( prices = [2,4,1]))