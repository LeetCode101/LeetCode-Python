import sys


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[-1] * n for _ in range(m)]

        for i in range(m):
            if s1[i] == s2[0]:
                dp[i][0] = i

        for j in range(1, n):
            start = -1

            for i in range(m):
                if s1[i] == s2[j]:
                    dp[i][j] = start

                start = max(start, dp[i][j - 1])

        min_length, start = sys.maxsize, -1

        for i in range(m):
            if dp[i][n - 1] == -1:
                continue

            current_length = i - dp[i][n - 1] + 1

            if current_length < min_length:
                min_length = current_length
                start = dp[i][n - 1]

        return s1[start:start + min_length] if start != -1 else ''
