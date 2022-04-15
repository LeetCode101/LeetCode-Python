from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) \
            -> List[List[str]]:
        row, column = click

        self._dfs(board, row, column)

        return board

    def _dfs(self, board, row, column):
        if board[row][column] == 'M':
            board[row][column] = 'X'

            return
        elif board[row][column] != 'E':
            return

        m, n = len(board), len(board[0])
        mine_count = 0
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0),
                      (1, 1), (0, 1), (-1, 1), (-1, 0)]

        for dx, dy in directions:
            next_row, next_column = row + dx, column + dy

            if 0 <= next_row < m and 0 <= next_column < n \
                    and board[next_row][next_column] == 'M':
                mine_count += 1

        if mine_count == 0:
            board[row][column] = 'B'
        else:
            board[row][column] = str(mine_count)

            return

        for dx, dy in directions:
            next_row, next_column = row + dx, column + dy

            if 0 <= next_row < m and 0 <= next_column < n:
                self._dfs(board, next_row, next_column)
