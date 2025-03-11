# 605. Can Place Flowers

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        # if len(flowerbed) >= 2:
        # if flowerbed[0] == 0 and flowerbed[1] == 0:
        #     flowerbed[0] = 1
        #     count -= 1
        # if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
        #     flowerbed[len(flowerbed) - 1] = 1
        #     count -= 1
        
        for i in range(len(flowerbed)-1):
            if count == 0:
                return True
            elif i == 0 or i == len(flowerbed) - 1:
                if flowerbed[0] == 0 and flowerbed[1] == 0:
                    flowerbed[0] = 1
                    count -= 1
                if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
                    flowerbed[len(flowerbed) - 1] = 1
                    count -= 1
            elif i > 0:
                if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    count -= 1
        return True if count <= 0 else False


print(Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(Solution().canPlaceFlowers(flowerbed = [1,0,1,0,1,0,1], n = 1))
print(Solution().canPlaceFlowers(flowerbed = [0,0,1,0,1], n = 1))
print(Solution().canPlaceFlowers(flowerbed = [0,0,1,0,0], n = 1))