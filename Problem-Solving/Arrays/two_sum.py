from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_context_main =  list()
        new_context =  set()

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and [nums[i], nums[j]] not in new_context_main:
                    if nums[i] < nums[j]:
                        new_context.add((nums[i], nums[j]))
                        new_context_main.append([i, j])
                    else:
                        new_context.add((nums[j], nums[i]))
                        new_context_main.append([i, j])

        print(new_context_main)
        
        for i in new_context_main:
            if i[0] != i[1]:
                return i
    
        return []
    

print(Solution().twoSum([0,4,3,0], 0))