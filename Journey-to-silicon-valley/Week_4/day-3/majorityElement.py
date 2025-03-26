# 229. Majority Element II

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        context = {}
        for number in nums:
            if context.get(number) != None:
                context[number] += 1
            else:
                context[number] = 1
        
        return [ key for key, value in context.items() if value > n / 3 ]
