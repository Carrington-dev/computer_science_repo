# 334. Increasing Triplet Subsequence

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] < nums[j] < nums[k] and i < j < k:
                        return True
        return False        

print(Solution().increasingTriplet(nums = [1,2,3,4,5]))
print(Solution().increasingTriplet(nums = [5,4,3,2,1]))