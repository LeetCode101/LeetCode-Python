from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = self._dfs(grid, i, j, visited)
                    max_area = max(area, max_area)

        return max_area

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1 or visited[row][column]:
            return 0

        area = 1
        visited[row][column] = True

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            area += self._dfs(grid, row + direction[0],
                              column + direction[1], visited)

        return area
