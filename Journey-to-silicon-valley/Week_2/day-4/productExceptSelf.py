# 238. Product of Array Except Self

from typing import List
# Exceeding Time Limit

def getProduct(arr):
    p = 1
    for i in arr:
        p *= i
    return p

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        context = [1 for i in nums]
        for i in range(len(nums)):
            context[i] = getProduct(nums[0: i] + nums[i+1:])
        return context
    
    def productExceptSelf(self, nums: List[int]):
        n = len(nums)

        # Initialize the result list as 1
        res = [1] * n

        for i in range(n):
            
            # Compute the product of all except nums[i]
            for j in range(n):
                if i != j:
                    res[i] *= nums[j]

        return res
        

print(Solution().productExceptSelf(nums = [1,2,3,4]))
print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))