from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(2)]
              for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0][0] = dp[i - 1][0][0]
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i])

        return dp[n - 1][1][0]
