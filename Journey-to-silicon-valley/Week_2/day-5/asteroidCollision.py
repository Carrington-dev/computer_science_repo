from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        context = deque()
        context.append(asteroids[0])
        for i in asteroids[1:]:
            if i < 0:
                if abs(i) < context[-1]:
                    pass

        return asteroids


print(Solution().asteroidCollision([5, 10, -5]))


"""
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""