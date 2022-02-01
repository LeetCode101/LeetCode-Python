from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        result = [-1] * n

        for i in range(n):
            result[i] = self._fall(grid, 0, i)

        return result

    def _fall(self, grid, row, column):
        m, n = len(grid), len(grid[0])

        if row == m:
            return column

        if grid[row][column] == 1:
            if column + 1 == n:
                return -1
            elif grid[row][column + 1] == -1:
                return -1
            else:
                return self._fall(grid, row + 1, column + 1)
        else:
            if column - 1 < 0:
                return -1
            elif grid[row][column - 1] == 1:
                return -1
            else:
                return self._fall(grid, row + 1, column - 1)
