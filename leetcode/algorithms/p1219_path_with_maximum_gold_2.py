from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        max_gold = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                max_gold = max(max_gold, self._dfs(grid, i, j, set()))

        return max_gold

    def _dfs(self, grid, row, column, visited):
        max_gold = 0
        m, n = len(grid), len(grid[0])

        visited.add((row, column))

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row = row + direction[0]
            next_column = column + direction[1]

            if next_row < 0 or next_row == m \
                    or next_column < 0 or next_column == n \
                    or grid[next_row][next_column] == 0 \
                    or (next_row, next_column) in visited:
                continue

            current_gold = self._dfs(grid, next_row, next_column, visited)
            max_gold = max(max_gold, current_gold)

            visited.remove((next_row, next_column))

        return max_gold + grid[row][column]
