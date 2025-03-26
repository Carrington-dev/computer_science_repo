# 204. Count Primes
class Solution:
    def getSeriesOfNSquared(self, n: int) -> int:
        
        if n < 2:
            return 0
        if n == 2:
            return 1

        primes = set()
        for i in range(2, n + 1):
            is_prime = True
            for num in primes:
                try:
                    if i % num != 0:
                        is_prime = False
                except:
                    pass
            if is_prime:
                primes.add(i)
        print(n, primes)
        return len(primes)


print(Solution().countPrimes(11))
print(Solution().countPrimes(12))
print(Solution().countPrimes(60))