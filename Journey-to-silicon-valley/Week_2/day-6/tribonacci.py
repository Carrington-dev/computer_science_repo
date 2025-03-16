"""
1137. N-th Tribonacci Number
Solved
Easy
Topics
Companies
Hint
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        context = [0, 1, 1]
        if n <= 2:
            return context[n]
        for i in range(3, n+1):
            context.append(context[i-1] +  context[i-2] + context[i-3])
        return context[n]


print(Solution().tribonacci(3))
print(Solution().tribonacci(4))
print(Solution().tribonacci(25))