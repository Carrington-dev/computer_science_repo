from collections import deque
from typing import List

"""
The app should run until there is no possible collision, 
that is until all asteroids are running the same direction
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = right = 0

        for i in asteroids:
            if i < 0:
                left += 1
            if i > 0:
                right += 1
                
        while not (right == 0 or left == 0):
            try:
                if asteroids[-1] < 0 and (asteroids[-2] > 0) :
                    if abs(asteroids[-1]) < abs(asteroids[-2]):
                        asteroids.pop()
                        left -= 1
                    elif abs(asteroids[-1]) > abs(asteroids[-2]):
                        asteroids[-2] = asteroids[-1]
                        asteroids.pop()
                        right -= 1
                    else:
                        asteroids.pop()
                        asteroids.pop()
                        right -= 1
                        left -= 1

            except:
                pass
            
            

        return asteroids


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision(asteroids = [8,-8]))
print(Solution().asteroidCollision([10,2,-5]))
print(Solution().asteroidCollision([-2,-1,1,2]))


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