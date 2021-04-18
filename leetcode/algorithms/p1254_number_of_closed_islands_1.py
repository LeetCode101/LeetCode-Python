from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0 and not visited[i][j] \
                        and self._dfs(i, j, grid, visited):
                    count += 1

        return count

    def _dfs(self, row, column, grid, visited):
        m = len(grid)
        n = len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n:
            return False

        if grid[row][column] == 1 or visited[row][column]:
            return 1

        closed = True
        visited[row][column] = True

        for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            closed &= self._dfs(row + direction[0],
                                column + direction[1], grid, visited)

        return closed
