from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        context =  { } # i:j for i, j in enumerate(prices)
        maximum =  -1
        minimum =  prices[0]

        for i in range(len(prices)):
            if maximum < prices[i]:
                maximum = prices[i]
                context[maximum] = i
            if minimum > prices[i]:
                minimum = prices[i]
                context[minimum] = i
        print(maximum, minimum)

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))