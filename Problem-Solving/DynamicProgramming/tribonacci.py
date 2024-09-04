class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_items = [0, 1, 1]
        for i in range(2, n+1):
            tribonacci_items.append(tribonacci_items[i - 1] + tribonacci_items[i - 2] + tribonacci_items[i - 3])
        
        return tribonacci_items[n + 1 ]
        

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

print(Solution().tribonacci(0))
print(Solution().tribonacci(25))
print(Solution().tribonacci(2))
print(Solution().tribonacci(3))
print(Solution().tribonacci(4))
print(Solution().tribonacci(5))