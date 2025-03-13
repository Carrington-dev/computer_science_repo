from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        try:
            while nums.index(0) < len(nums) - nums.count(0) :
                for i in range(len(nums) - 1):
                    if nums[i] == 0:
                        nums[i], nums[1+i] = nums[i+1], nums[i]
        except:
            pass
        return nums

print(Solution().moveZeroes(nums = [0,1,0,3,12]))
print(Solution().moveZeroes(nums = [ 0]))