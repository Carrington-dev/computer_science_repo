from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        print(s)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j  = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1
    

print(Solution().reverseString(["h","e","l","l","o"]))
print(Solution().reverseString(["H","a","n","n","a","h"]))