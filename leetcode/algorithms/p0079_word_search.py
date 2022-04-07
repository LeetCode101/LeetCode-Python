from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]

                if self._dfs(board, i, j, word, 0, len(word) - 1, visited):
                    return True

        return False

    def _dfs(self, board, row, column, word, start, end, visited):
        m, n = len(board), len(board[0])

        if row < 0 or row == m or column < 0 or column == n or visited[row][column] or board[row][column] != word[start]:
            return False

        if start == end:
            return True

        visited[row][column] = True

        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            next_row = row + dx
            next_column = column + dy

            if 0 <= next_row < m and 0 <= next_column < n and not visited[next_row][next_column] and board[next_row][next_column] == word[start + 1]:
                found = self._dfs(board, next_row, next_column, word, start + 1, end, visited)

                if found:
                    return True
                else:
                    visited[next_row][next_column] = False

        return False
