# 2364. Count Number of Bad Pairs

from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and j - i != nums[j] - nums[i]:
                    count += 1
        
        return count


print(Solution().countBadPairs(nums = [4,1,3,3]))