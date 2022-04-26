class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i

            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j - 2 + 1))

        return dp[-1]
