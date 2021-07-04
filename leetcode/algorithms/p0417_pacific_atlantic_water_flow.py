from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        pacific_connected = [[False] * n for _ in range(m)]
        atlantic_connected = [[False] * n for _ in range(m)]
        result = []

        for i in range(m):
            self._dfs(heights, i, 0, pacific_connected, m, n)
            self._dfs(heights, i, n - 1, atlantic_connected, m, n)

        for i in range(n):
            self._dfs(heights, 0, i, pacific_connected, m, n)
            self._dfs(heights, m - 1, i, atlantic_connected, m, n)

        for i in range(m):
            for j in range(n):
                if pacific_connected[i][j] and atlantic_connected[i][j]:
                    result.append([i, j])

        return result

    def _dfs(self, heights, row, column, connected, m, n):
        connected[row][column] = True

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_column = row + direction[0], column + direction[1]

            if new_row < 0 or new_row >= m \
                    or new_column < 0 or new_column >= n \
                    or connected[new_row][new_column] \
                    or heights[row][column] > heights[new_row][new_column]:
                continue

            self._dfs(heights, new_row, new_column, connected, m, n)
