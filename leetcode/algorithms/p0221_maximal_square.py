from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_width = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = \
                        min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    max_width = max(max_width, dp[i + 1][j + 1])

        return max_width * max_width
