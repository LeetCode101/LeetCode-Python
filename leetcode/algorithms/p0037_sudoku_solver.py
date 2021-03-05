from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for column in range(9):
                if board[row][column] != '.':
                    continue

                for number in range(1, 10):
                    if self._is_valid(board, row, column, str(number)):
                        board[row][column] = str(number)

                        if self._solve(board):
                            return True
                        else:
                            board[row][column] = '.'

                return False

        return True

    def _is_valid(self, board: List[List[str]], row: int,
                  column: int, number: str) -> bool:
        for i in range(9):
            if board[i][column] == number:
                return False

            if board[row][i] == number:
                return False

            box_row = 3 * (row // 3) + i // 3
            box_column = 3 * (column // 3) + i % 3

            if board[box_row][box_column] == number:
                return False

        return True
