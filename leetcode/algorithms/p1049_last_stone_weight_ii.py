from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = len(stones)
        dp = [[0] * (total // 2 + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, total // 2 + 1):
                if j >= stones[i - 1]:
                    current = dp[i - 1][j - stones[i - 1]] + stones[i - 1]
                    dp[i][j] = max(dp[i - 1][j], current)
                else:
                    dp[i][j] = dp[i - 1][j]

        return total - dp[n][total // 2] * 2
