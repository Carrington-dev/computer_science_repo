from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        print(board)

print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))