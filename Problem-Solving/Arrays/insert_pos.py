from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            if nums.index(target) >= 0:
                return nums.index(target)
        except:  
            if target < nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            count = 0
            while count < len(nums):
                if nums[count] < target and target < nums[count+1]:
                    return count + 1
                count += 1
        return 0
    
print(Solution().searchInsert(nums = [1,3,5,6], target = 5))
print(Solution().searchInsert(nums = [1,3,5,6], target = 2))
print(Solution().searchInsert(nums = [1,3,5,6], target = 7))