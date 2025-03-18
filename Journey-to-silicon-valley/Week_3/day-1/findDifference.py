class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)
        context = [[], []]
        for i in num1:
            if i not in num2:
                context[0].append(i)
        for j in num2:
            if j not in num1:
                context[1].append(j)
        return context
