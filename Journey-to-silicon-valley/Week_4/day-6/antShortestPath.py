from typing import List
from collections import deque

class Solution:
    def antMoves(self, grid: List[List[int]]) -> int:
        def getNeighbours(x, y, length_of_grid, length_of_item):
            neighbours =  [ (x, y+1), (x+1, y), (x-1, y), (x, y-1),  (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1) ]
            return [ (x, y) for (x, y) in neighbours if x >= 0 and y >= 0 and x < length_of_grid and y < length_of_item ]
        stack = deque()
        stack.append((0, 0))
        context = {}
        parents = {}

        count = 0
        all_points = []
        while len(stack) > 0:
            x, y = stack.pop()
            context[(x, y)] = True
            neighbours = getNeighbours(x, y, len(grid), len(grid[0]))
            for (neighbour_x, neighbour_y) in neighbours:
                if grid[neighbour_x][neighbour_y] > grid[x][y]:
                    if not context.get((neighbour_x, neighbour_y)):
                        stack.append((neighbour_x, neighbour_y))
                        all_points.append((neighbour_x, neighbour_y))
                        parents[(neighbour_x, neighbour_y)] = (x, y)
            count += 1
        return all_points

print(Solution().antMoves(grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
print(Solution().antMoves(grid = [[3,2,4],[2,1,9],[1,1,7]]))