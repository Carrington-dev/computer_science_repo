from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        context = {}
        for i in nums:
            if context.get(i) == None:
                context[i] = 1
            else:
                return True
        return False
    
print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))