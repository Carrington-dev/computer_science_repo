# 1431. Kids With the Greatest Number of Candies
# Easy
# Hint
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxxed = candies[0]
        for i in candies:
            if maxxed < i:
                maxxed = i

        candiesGreater = [ False for i in candies ]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxxed:
                candiesGreater[i] = True
        
        return candiesGreater

print(Solution().kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))