from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [i ^ (i // 2) for i in range(pow(2, n))]
        return result
    

print(Solution().grayCode(2))
print(Solution().grayCode(3))
print(Solution().grayCode(1))