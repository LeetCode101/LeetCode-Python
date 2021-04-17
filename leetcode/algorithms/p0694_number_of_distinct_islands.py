from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        paths = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    paths.add(self._dfs(grid, i, j))

        return len(paths)

    def _dfs(self, grid, row, column):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1:
            return ''

        grid[row][column] = 0
        full_path = ''

        directions = ['u', 'l', 'd', 'r']
        for i, direction in enumerate([[-1, 0], [0, -1], [1, 0], [0, 1]]):
            full_path += self._dfs(grid, row + direction[0],
                                   column + direction[1]) + directions[i]

        return full_path + 'c'
