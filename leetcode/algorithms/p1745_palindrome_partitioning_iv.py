class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]

        for i in range(1, n):
            for j in range(i + 1, n):
                if dp[0][i - 1] and dp[i][j - 1] and dp[j][n - 1]:
                    return True

        return False
