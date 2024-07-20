from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1
        i, j = 0, 0

        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[ i + j ] = temp[i]
                i += 1
            elif temp[i] > nums2[j]:
                nums1[i + j] = nums2[j]
                j += 1
            else:
                nums1[ i + j ] = temp[i]
                i += 1
                nums1[i + j ] = nums2[j]
                j += 1

        print(temp)
        print(nums1)
        print(nums2)
        while i < m:
            nums1[i+j] = temp[i]
            i += 1

        while j < n:
            nums1[i + j] = nums2[j]
            j += 1

        return nums1
    
    def mergeSlowly(self, nums1, nums2):
        return sorted([i for i in (nums1 + nums2) if i != 0])
    
print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(Solution().mergeSlowly(nums1=[1,2,3,0,0,0] , nums2= [2,5,6]))