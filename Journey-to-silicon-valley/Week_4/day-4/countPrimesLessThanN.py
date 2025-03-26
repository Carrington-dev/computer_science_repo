# 204. Count Primes
class Solution:

    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5 + 1) ):
                if n % i == 0:
                    return False
            return True
        
        primes = set()
        for i in range(n):
            if isPrime(i):
                primes.add(i)
        # print(primes)
        return len(primes)
        
        

print(Solution().countPrimes(11))
print(Solution().countPrimes(12))
print(Solution().countPrimes(60))