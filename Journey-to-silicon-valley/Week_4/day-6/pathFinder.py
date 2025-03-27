from collections import deque
import csv
from typing import List


class Solution:
    def __init__(self, x, y):
        self.grid = None

    def printGrid(self):
        for i in self.grid:
            for j in i:
                print(j, sep=" ", end=" ")
            print()

    def readGrid(self):
        with open('Journey-to-silicon-valley/Week_4/day-6/ants-1.txt', 'r') as f:
            csvreader = list(csv.reader(f))
            grid = []
            for i in csvreader:
                grid.append(list(i[0]))
            self.grid = grid
    
    def maxMoves(self, start_x, start_y) -> int:
        def getNeighbours(x, y, length_of_grid, length_of_item):
            neighbours =  [ (x, y+1), (x+1, y), (x-1, y), (x, y-1),  (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1) ]
            return [ (x, y) for (x, y) in neighbours if x >= 0 and y >= 0 and x < length_of_grid and y < length_of_item ]
        
        grid = self.grid
        stack = deque()
        stack.append((0, 0))
        context = {}

        count = 0
        parent = {}
        previous = start_x, start_y
        while len(stack) > 0:
            x, y = stack.pop()
            context[(x, y)] = True
            neighbours = getNeighbours(x, y, len(grid), len(grid[0]))
            # print(neighbours)
            for (neighbour_x, neighbour_y) in neighbours:
                if grid[neighbour_x][neighbour_y] != "x":
                    if not context.get((neighbour_x, neighbour_y)):
                        if grid[neighbour_x][neighbour_y] == "S":
                                parent[(neighbour_x, neighbour_y)] = (x, y)
                                stack.append((neighbour_x, neighbour_y))
                                print("Reached S")
                                break
                        parent[(neighbour_x, neighbour_y)] = (x, y)
                        previous = (neighbour_x, neighbour_y)
                    
            count += 1
            # print(parent)

        length = 0
        # end_x, end_y = stack.pop()
        end_x, end_y = (neighbour_x, neighbour_y)
        while (end_x, end_y) != (start_x, start_y):
            self.grid[end_x][end_y] = "*"
            (end_x, end_y) = parent[(end_x, end_y)]
            length += 1
        return length

a = Solution(14, 17)
a.readGrid()
a.printGrid()
print()
a.maxMoves(3, 14)
a.printGrid()
