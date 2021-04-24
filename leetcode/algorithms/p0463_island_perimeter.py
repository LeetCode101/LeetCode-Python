from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter
