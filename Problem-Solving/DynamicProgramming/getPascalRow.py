from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        pascalTriangle = [[1], [1, 1]]
        
        for i in range(2, numRows):
            newItem = [1]
            for j in range(1, i):
               newItem.append(pascalTriangle[i - 1][j - 1] + pascalTriangle[i - 1][j])
            newItem += [1]
            pascalTriangle.append(newItem)

        return pascalTriangle[rowIndex]
    
print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(5))
print(Solution().getRow(10))