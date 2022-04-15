import collections
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) \
            -> List[List[str]]:
        m, n = len(board), len(board[0])
        queue = collections.deque([click])

        while queue:
            row, column = queue.popleft()

            if board[row][column] == 'M':
                board[row][column] = 'X'

                break
            elif board[row][column] != 'E':
                continue

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

                continue

            for dx, dy in directions:
                next_row, next_column = row + dx, column + dy

                if 0 <= next_row < m and 0 <= next_column < n:
                    queue.append((next_row, next_column))

        return board
