from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[1], [1, 1]]
        if numRows <= 2:
            return pascalTriangle[:numRows]
        
        for i in range(2, numRows):
            newItem = [1]
            for j in range(1, i):
               newItem.append(pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j])
            newItem += [1]
            pascalTriangle.append(newItem)

        return pascalTriangle
    
print(Solution().generate(0))
print(Solution().generate(1))
print(Solution().generate(2))
print(Solution().generate(3))
print(Solution().generate(5))
print(Solution().generate(6))