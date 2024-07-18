class Solution:
    # def climbStairs(self, n: int) -> int:
    #     # if n == 1 or n == 2:
    #     #     return n
        
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    def climbStairs(self, n: int) -> int:
        nums = [0, 1, 2]
        for i in range(3, n+1):
            nums.append(nums[i-1] + nums[i-2])
        return nums[n]


print(Solution().climbStairs(5))
print(Solution().climbStairs(44))