from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter = { v:k for k, v in counter.items() }
        return counter[1]
    
print(Solution().singleNumber(nums = [4,1,2,1,2]))
print(Solution().singleNumber(nums = [2,2,3,2]))