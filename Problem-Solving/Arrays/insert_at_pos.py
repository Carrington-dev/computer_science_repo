from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        while count < len(nums):
            if nums[count] > target:
                return count
            if nums[count] == target:
                return count
            count += 1
        
        return count
            
    
print(Solution().searchInsert(nums = [1,3,5,6], target = 5))
print(Solution().searchInsert(nums = [1,3,5,6], target = 2))
print(Solution().searchInsert(nums = [1,3,5,6], target = 7))