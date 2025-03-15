from typing import List
from itertools import permutations

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        original = nums
        sorted_arr = sorted(nums)
        list_of_perm = sorted(set(permutations(sorted_arr)))
        # print(list_of_perm)
        for i in range(len(list_of_perm)):
            if list_of_perm[i] == tuple(original):
                if i <= len(list_of_perm) - 2:
                    verdict = list(list_of_perm[i + 1])
                    for j in range(len(verdict)):
                        nums[j] = verdict[j]
                    return nums
                elif i == len(list_of_perm) - 1:
                    verdict = list(list_of_perm[0])
                    for j in range(len(verdict)):
                        nums[j] = verdict[j]
                    return nums

        return nums


print(Solution().nextPermutation([1, 2, 3]))
print(Solution().nextPermutation([3,2,1]))
print(Solution().nextPermutation([1,1,5]))
print(Solution().nextPermutation([1,5,1]))