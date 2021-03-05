from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            column = [row[i] for row in board]

            if not self._is_valid(column):
                return False

        for i, row in enumerate(board):
            if not self._is_valid(row):
                return False

        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                boxes = board[row][column:column + 3] + \
                        board[row + 1][column:column + 3] + \
                        board[row + 2][column:column + 3]

                if not self._is_valid(boxes):
                    return False

        return True

    def _is_valid(self, numbers: List[str]) -> bool:
        visited = set()

        for n in numbers:
            if n == '.':
                continue

            if n in visited:
                return False
            else:
                visited.add(n)

        return True
