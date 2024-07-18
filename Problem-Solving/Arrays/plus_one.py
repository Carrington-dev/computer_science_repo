from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        isSolved = False
        counter = 1
        while not isSolved:
            try:
                digits[ -1 * counter]
            except IndexError:
                digits = [ 0 ] + digits
            if digits[-1 * counter] != 9:
                digits[ -1 * counter] += 1
                isSolved = True
            else:
                digits[ -1 * counter] = 0
            counter += 1
        return digits
    

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([1,2,9]))
print(Solution().plusOne([1,9,9]))
print(Solution().plusOne([4,3, 2, 1]))
print(Solution().plusOne([9]))
print(Solution().plusOne([0, 1, 9]))