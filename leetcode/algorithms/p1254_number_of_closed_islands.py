from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += self._dfs(i, j, grid)

        return count

    def _dfs(self, row, column, grid):
        m = len(grid)
        n = len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n:
            return 0

        if grid[row][column] == 1:
            return 1

        grid[row][column] = 1
        edges = 0

        for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            edges += self._dfs(row + direction[0], column + direction[1], grid)

        return 1 if edges == 4 else 0
