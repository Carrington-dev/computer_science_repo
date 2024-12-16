class Solution:
    def reverseBits(self, n: int) -> int:
        return (str(n)[::-1])
    
print(Solution().reverseBits('00000010100101000001111010011100'))
print(Solution().reverseBits('11111111111111111111111111111101'))