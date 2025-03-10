from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [ 1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product[i] *= nums[j]
        return product



print(Solution().productExceptSelf(nums = [1,2,3,4]))
print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))