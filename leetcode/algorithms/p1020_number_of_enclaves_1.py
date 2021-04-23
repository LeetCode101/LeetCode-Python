from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        enclaves = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    area, has_boundary = self._dfs(grid, i, j, visited)

                    if not has_boundary:
                        enclaves += area

        return enclaves

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1 or visited[row][column]:
            return 0, row < 0 or row >= m or column < 0 or column >= n

        area = 1
        visited[row][column] = True
        has_boundary = self._is_boundary(m, n, row, column)

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            neighbour_area, neighbour_has_boundary = self._dfs(
                grid, row + direction[0],
                column + direction[1], visited)
            area += neighbour_area
            has_boundary = has_boundary or neighbour_has_boundary

        return area, has_boundary

    def _is_boundary(self, m, n, row, column):
        return row == 0 or row == m - 1 or column == 0 or column == n - 1
