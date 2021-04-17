from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        paths = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    paths.add(self._dfs(grid, i, j, visited))

        return len(paths)

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1 or visited[row][column]:
            return ''

        visited[row][column] = True
        full_path = ''

        directions = ['u', 'l', 'd', 'r']
        for i, direction in enumerate([[-1, 0], [0, -1], [1, 0], [0, 1]]):
            path = self._dfs(grid, row + direction[0],
                             column + direction[1], visited)
            full_path += path + directions[i]

        return full_path + 'c'
