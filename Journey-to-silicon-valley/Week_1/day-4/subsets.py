# 90. Subsets II

from itertools import combinations
from typing import List


# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # subsets = []
        # for i in range(len(nums) + 1):
        #     for j in range(len(nums) + 1):
        #         subsets.append(nums[i:j])
        
        # return subsets
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_numbers = [[(j) for j in set(combinations(nums, i)) ] for i in range(len(nums) + 1) ]
        all_numbers_list = set()
        for i in all_numbers:
            for j in i:
                all_numbers_list.add(tuple(sorted(j,)))
        return list([ list(i) for i in all_numbers_list])
    
print(Solution().subsetsWithDup([1, 2, 3]))
print(Solution().subsetsWithDup([1, 2, 2]))
print(Solution().subsetsWithDup([ 0 ]))
print(Solution().subsetsWithDup([4,4,4,1,4]))