from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = self.findMergeSortedArrays(nums1, nums2)
        length = len(new_arr)
        if length == 0:
            return None
        elif length % 2 == 0:
            # print(((length ) // 2 - 1, ((length ) // 2 )))
            return (new_arr[ ((length ) // 2 - 1) ]  + new_arr[ ((length ) // 2 ) ]) / 2 
            # return (new_arr[ int((length ) / 2) ]  + new_arr[ int((length ) / 2 + 1) ]) / 2
        return new_arr[ (length ) // 2 ]
        
    def findMergeSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print("nums1 = ", nums1, "nums2 = ", nums2)
        i = 0
        j = 0
        new_list = [ 0 for i in range(len(nums1)+len(nums2))]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_list[ i + j ] = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                new_list[ i + j ] = nums2[j]
                j += 1
            else:
                new_list[ i + j ] = nums1[i]
                new_list[ i + j + 1 ] = nums2[j]
                i += 1
                j += 1

        
        while i < len(nums1):
            new_list[ i + j ] = nums1[i]
            i += 1


        while j < len(nums2):
            new_list[ i + j ] = nums2[j]
            j += 1

        return new_list
    

print(Solution().findMergeSortedArrays([1,2], [3,4]))
print(Solution().findMergeSortedArrays([i for i in range(0, 13) if i % 2 == 1 ], [i for i in range(0, 13) if i % 2 == 0]))

print(Solution().findMedianSortedArrays([1,2], [3,4]))
print(Solution().findMedianSortedArrays([i for i in range(0, 13) if i % 2 == 1 ], [i for i in range(0, 13) if i % 2 == 0]))
