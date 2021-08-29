from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        prefix_sum = [i for i in stones]

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                take_left = self._get_sum(prefix_sum, i + 1, j) - dp[i + 1][j]
                take_right = self._get_sum(prefix_sum, i, j - 1) - dp[i][j - 1]
                dp[i][j] = max(take_left, take_right)

        return dp[0][-1]

    def _get_sum(self, prefix_sum, i, j):
        if i == 0:
            return prefix_sum[j]
        else:
            return prefix_sum[j] - prefix_sum[i - 1]
