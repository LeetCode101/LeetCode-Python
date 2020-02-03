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

                    self.dfs(grid, visited, i, j)

        return count

    def dfs(self, grid: List[List[str]], visited: List[List[bool]],
            row: int, column: int) -> None:
        m, n = len(grid), len(grid[0])
        visited[row][column] = True

        if row - 1 >= 0 and grid[row - 1][column] == '1' \
                and not visited[row - 1][column]:
            self.dfs(grid, visited, row - 1, column)

        if row + 1 <= m - 1 and grid[row + 1][column] == '1' \
                and not visited[row + 1][column]:
            self.dfs(grid, visited, row + 1, column)

        if column - 1 >= 0 and grid[row][column - 1] == '1' \
                and not visited[row][column - 1]:
            self.dfs(grid, visited, row, column - 1)

        if column + 1 <= n - 1 and grid[row][column + 1] == '1' \
                and not visited[row][column + 1]:
            self.dfs(grid, visited, row, column + 1)
