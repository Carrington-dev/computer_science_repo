# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] == nums[j] and abs(i - j) <= k:
                        count += 1
        
        return True if count == 2 else False
