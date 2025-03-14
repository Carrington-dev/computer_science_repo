# 15. 3Sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        context = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                        context.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        return list(context)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        context = set()
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    context.add((nums[i], nums[j], nums[k]))
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return [ list(i) for i in context ]

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))
print(Solution().threeSum(nums = [0,1,1]))
print(Solution().threeSum(nums = [0,0,0]))