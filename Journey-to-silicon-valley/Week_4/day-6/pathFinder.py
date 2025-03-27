import csv


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
            
a = Solution(14, 17)
a.readGrid()
a.printGrid()
