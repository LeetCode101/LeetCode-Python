from typing import List


class Solution:
    def __init__(self):
        self.max_gold = 0

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                self._dfs(grid, i, j, set(), grid[i][j])

        return self.max_gold

    def _dfs(self, grid, row, column, visited, gold_so_far):
        m, n = len(grid), len(grid[0])

        visited.add((row, column))

        self.max_gold = max(self.max_gold, gold_so_far)

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row = row + direction[0]
            next_column = column + direction[1]

            if next_row < 0 or next_row == m \
                    or next_column < 0 or next_column == n \
                    or grid[next_row][next_column] == 0 \
                    or (next_row, next_column) in visited:
                continue

            self._dfs(grid, next_row, next_column, visited,
                      gold_so_far + grid[next_row][next_column])

            visited.remove((next_row, next_column))
