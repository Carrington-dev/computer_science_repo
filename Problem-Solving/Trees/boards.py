from collections import deque


class Maze:
    def __init__(self, file, starting_row, starting_col, ending_row, ending_col, x, y) -> None:
        self.board = []
        self.file = file
        self.starting_row = starting_row
        self.starting_col = starting_col
        self.ending_row = ending_row
        self.ending_col = ending_col
        self.length = y
        self.width = x
        self.read_board()
        print()
        print(self.width, self.length)
        # self.traverse()
        
    def print(self):
        for i in self.board:
            print(" ".join(i).replace("\n", ""))

    def read_board(self):
        with open(self.file, "r") as f:
            for i in f.readlines():
                self.board.append(i.split(" "))
                
    def traverse(self):
        queue = deque()
        visited = set()
        queue.append((self.starting_row, self.starting_col))
        while len(queue) > 0:
            x, y = (queue.pop())
            self.board[x][y] = "*"
            if x == self.starting_row and y == self.starting_col:
                self.board[x][y] = "S"
            if x == self.ending_row and y == self.ending_col:
                self.board[x][y] = "F"
                return "Solved"

            visited.add((x, y))
            for _x, _y in self._move_on_coordinates(x, y):
                    if _x < self.width and self.length > _y:
                        if (self.board[_x][_y]) != 'x':
                            if (_x, _y) not in visited:
                                queue.append((_x, _y))
        return "No path"
        
    def _move_on_coordinates(self, row, col):
        coordinates = []
        if row + 1 < self.width:
            coordinates.append((row + 1, col))
        if row - 1 >= 0:
            coordinates.append((row - 1, col))
        if col + 1 < self.length:
            coordinates.append((row, col + 1))
        if col - 1 >= 0:
            coordinates.append((row, col - 1))
        return coordinates

maze = Maze("board.txt", 1, 1, 21, 19, 23, 21)
# maze = Maze("maze1.txt", starting_row=3, starting_col=13, ending_row=11, ending_col=10, x=14, y=17)
maze.print()
maze.traverse()
maze.print()