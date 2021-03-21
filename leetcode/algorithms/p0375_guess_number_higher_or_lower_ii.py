class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for low in range(n, 0, -1):
            for high in range(low + 1, n + 1):
                dp[low][high] = min(x + max(dp[low][x - 1], dp[x + 1][high])
                                    for x in range(low, high))
        return dp[1][n]
