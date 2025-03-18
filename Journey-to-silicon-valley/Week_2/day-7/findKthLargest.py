class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
        # if k == 1:
        #     return nums[-k]
        # if nums[-k] != nums[-k+1]:
        #     return nums[-k]
        # return self.findKthLargest(nums[:-k], k)
