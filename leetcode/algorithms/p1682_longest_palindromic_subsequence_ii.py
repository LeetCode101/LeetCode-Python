class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        chars = [[''] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and s[i] != chars[i + 1][j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    chars[i][j] = s[i]
                else:
                    if dp[i + 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i + 1][j]
                        chars[i][j] = chars[i + 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
                        chars[i][j] = chars[i][j - 1]

        return dp[0][n - 1]
