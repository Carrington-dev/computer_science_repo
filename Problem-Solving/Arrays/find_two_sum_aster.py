from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return sorted([i, j])

        return []
    


print(Solution().twoSum([0,4,3,0], 0))
print(Solution().twoSum([0,4,3,0], 7))