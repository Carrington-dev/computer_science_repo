class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        left = 0
        right = len(s) - 1
        while (left < right):
            if s[left:right].count("R") == s[left:right].count("L"):
                left += 1
                count += 1
            elif s[:left].count("R") == s[:left].count("L"):
                left += 1
                count += 1
        return count
    
print(Solution().balancedStringSplit(s = "RLRRLLRLRL"))
print(Solution().balancedStringSplit(s = "RLRRRLLRLL"))