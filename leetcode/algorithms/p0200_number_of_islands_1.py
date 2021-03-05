from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1

                    self._dfs(grid, i, j, visited)

        return count

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != '1' or visited[row][column]:
            return

        visited[row][column] = True

        self._dfs(grid, row - 1, column, visited)
        self._dfs(grid, row + 1, column, visited)
        self._dfs(grid, row, column - 1, visited)
        self._dfs(grid, row, column + 1, visited)
