
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return str(bin(int(a, 2) + int(b, 2))).replace("0b", "")
        return str(bin(int(a, 2) + int(b, 2)))[2:]
    
print(Solution().addBinary("00101", "100"))
print(Solution().addBinary("101", "100"))
print(Solution().addBinary("0101", "100"))
print(Solution().addBinary(a = "1010", b = "1011"))
print(Solution().addBinary(a = "11", b = "01"))
print(Solution().addBinary(a = "0", b = "0"))