class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s2), len(s1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = i + 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        start, min_length = 0, n + 1

        for i in range(1, n + 1):
            if dp[m][i] != 0 and i - dp[m][i] + 1 < min_length:
                start = dp[m][i] - 1
                min_length = i - dp[m][i] + 1

        return '' if min_length == n + 1 else s1[start:start + min_length]
