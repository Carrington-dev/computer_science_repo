class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n == 1): return True
        elif( n < 4): return False
        while( n % 4 == 0):
            n = n / 4
        return True if n == 1 else False
    

for i in range(220):
    if(Solution().isPowerOfFour(i)):
        print(i, " => ", Solution().isPowerOfFour(i))

print(128, " => ", Solution().isPowerOfFour(128))