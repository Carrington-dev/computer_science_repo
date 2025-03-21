from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = lount = 0
        maximum = 0
        start = end = 0
        kount = k
        for i in range(len(nums)):
            # if count > maximum:
            #     maximum = count
            if nums[i] == 1:
                count += 1
                if count > maximum:
                    maximum = count
                end = i
            else:
                if count > maximum:
                    maximum = count
                count = 0
                start = i
        while kount > 0:
            # print("Running")
            try:
                if nums[end - 1] != 1:
                    nums[end - 1] = 1
                    end  = end -1
                    kount -= 1
                    count += 1
                    if count > maximum:
                        maximum = count
                else:
                    end  = end -1
            except:
                pass
        
        count = lount = 0
        maximum = 0
        for i in range(len(nums)):
            # if count > maximum:
            #     maximum = count
            if nums[i] == 1:
                count += 1
                lount += 1
                if count > maximum:
                    maximum = count
                end = i
            else:
                if count > maximum:
                    maximum = count
                count = 0
                start = i
        print(nums)
        return maximum


print(Solution().longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(Solution().longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))