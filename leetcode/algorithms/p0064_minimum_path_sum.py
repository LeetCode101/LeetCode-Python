import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    left = dp[i][j - 1] if j - 1 >= 0 else sys.maxsize
                    up = dp[i - 1][j] if i - 1 >= 0 else sys.maxsize
                    dp[i][j] = grid[i][j] + min(left, up)

        return dp[-1][-1]
