class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 == 1:
            return False
        while n > 0:
            if n == 1:
                return True
            elif n % 2 == 1:
                return False
            n = n / 2
        
        return False


print(Solution().isPowerOfTwo(567))
print(Solution().isPowerOfTwo(512))
print(Solution().isPowerOfTwo(1012))
print(Solution().isPowerOfTwo(1024))