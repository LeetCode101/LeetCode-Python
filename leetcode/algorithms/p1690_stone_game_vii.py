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
                dp[i][j] = max(prefix_sum[j] - prefix_sum[i + 1] - dp[i + 1][j],
                               prefix_sum[j - 1] - prefix_sum[i] - dp[i][j - 1])

        return dp[0][-1]
