import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                left = dp[i][j - 1] if j - 1 >= 0 else sys.maxsize
                up = dp[i - 1][j] if i - 1 >= 0 else sys.maxsize
                lower = min(left, up)
                dp[i][j] = grid[i][j] + (lower if lower != sys.maxsize else 0)

        return dp[-1][-1]
