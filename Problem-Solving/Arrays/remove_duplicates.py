from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list_set = list(set(nums))  
        nums.clear()
        return (list_set)
    


print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(Solution().removeDuplicates([1,1,2]))