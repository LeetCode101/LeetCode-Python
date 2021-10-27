from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        found = False
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                found = self._paint(grid, i, j) > 0

                if found:
                    break

            if found:
                break

        color = 2

        while True:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == color and (self._expand(grid, i - 1, j, color) or self._expand(grid, i, j - 1, color) or self._expand(grid, i + 1, j, color) or self._expand(grid, i, j + 1, color)):
                        return color - 2

            color += 1

    def _paint(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0

        grid[i][j] = 2

        return 1 + self._paint(grid, i + 1, j) + self._paint(grid, i - 1, j) + self._paint(grid, i, j + 1) + self._paint(grid, i, j - 1)

    def _expand(self, grid, i, j, color):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
            return False

        if grid[i][j] == 0:
            grid[i][j] = color + 1

        return grid[i][j] == 1
