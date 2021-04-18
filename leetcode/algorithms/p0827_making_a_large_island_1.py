from typing import List


# Time Limit Exceeded!
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    new_grid = self._new_grid(grid, m, n, i, j)
                    area = self._max_area_of_island(new_grid)
                    max_area = max(area, max_area)

        return max_area if max_area != 0 else self._max_area_of_island(grid)

    def _max_area_of_island(self, grid: List[List[int]]) -> int:
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

    def _new_grid(self, grid, m, n, row, column):
        new_grid = [[grid[i][j] for j in range(n)] for i in range(m)]
        new_grid[row][column] = 1

        return new_grid
