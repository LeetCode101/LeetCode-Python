class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        if not s:
            return True

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        removed = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            removed[i][i] = 0

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    removed[i][j] = removed[i + 1][j - 1]
                else:
                    if dp[i + 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i + 1][j]
                        removed[i][j] = 1 + removed[i + 1][j]
                    elif dp[i + 1][j] < dp[i][j - 1]:
                        dp[i][j] = dp[i][j - 1]
                        removed[i][j] = 1 + removed[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1]
                        removed[i][j] = 1 + min(
                            removed[i][j - 1], removed[i + 1][j])

        return dp[0][n - 1] > 0 and removed[0][n - 1] <= k
