import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        connected_with_border = [[False] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]

        for row in range(m):
            for column in range(n):
                if row == 0 or row == m - 1 or column == 0 or column == n - 1:
                    self._search(board, row, column,
                                 connected_with_border, visited)

        for row in range(m):
            for column in range(n):
                if not connected_with_border[row][column] \
                        and board[row][column] == 'O':
                    board[row][column] = 'X'

    def _search(self, board, row, column, connected_with_board, visited):
        if board[row][column] == 'X' or visited[row][column]:
            return

        m, n = len(board), len(board[0])
        connected_with_board[row][column] = True
        queue = collections.deque([(row, column)])

        while queue:
            row, column = queue.popleft()

            if visited[row][column]:
                continue

            visited[row][column] = True

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_row, next_column = row + dx, column + dy

                if 0 <= next_row < m and 0 <= next_column < n \
                        and not visited[next_row][next_column] \
                        and board[next_row][next_column] == 'O':
                    connected_with_board[next_row][next_column] = True
                    queue.append((next_row, next_column))
