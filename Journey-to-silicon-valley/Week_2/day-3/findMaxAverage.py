from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        for i in range(0, len(nums) - k + 1):
            other_sum =  sum(nums[i:k+i])
            if other_sum > max_sum:
                max_sum = other_sum
        return max_sum / k

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         possible_list = sorted(nums)[::-1][:k]
#         return sum(possible_list) / k

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#        curr_sum = max_sum = sum(nums[:k]) # current sum and max sum assign to be sums of nums till k non inclusive
#        for i in range(len(nums)-k): #loop will run through the length of nums till we can form the last subarray
#             curr_sum += nums[i + k] - nums[i] #updating currsum by adding new k elemt and subtracting first elmt
#             max_sum = max(max_sum, curr_sum) #updating max if found
#        return max_sum/k #returning max by dividing it by k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], k = 4))
print(Solution().findMaxAverage([1,12,3], k = 2))
print(Solution().findMaxAverage([1,-12,3], k = 2))
print(Solution().findMaxAverage(nums = [5], k = 1))
print(Solution().findMaxAverage(nums = [0,1,1,3,3], k = 4))