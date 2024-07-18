from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = [ i for i in nums if (i != val) ]
        return f"{len(a)}, nums = {a} "
    


# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeElement([0,1,2,2,3,0,4,2], val = 2))