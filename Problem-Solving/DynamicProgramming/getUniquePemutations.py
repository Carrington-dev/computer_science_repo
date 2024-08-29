from typing import List
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(i) for i in list(set(permutations(nums)))
]
print(Solution().permuteUnique([1, 1, 2]))
print(Solution().permuteUnique([1, 2, 3]))
print(Solution().permuteUnique([2, 4]))
print(Solution().permuteUnique([5, 7,5,3]))
print(Solution().permuteUnique([9,5]))