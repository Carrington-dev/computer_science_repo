# 41. First Missing Positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums =  set(nums)
        i = 1
        while i in nums:
            i += 1
        return i
