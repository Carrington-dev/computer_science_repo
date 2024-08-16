class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count("1")
    
print(Solution().hammingWeight(128))
print(Solution().hammingWeight(11))
print(Solution().hammingWeight(13))
print(Solution().hammingWeight(3))