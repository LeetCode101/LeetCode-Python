from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]

        for i in range(1, length + 1):
            zero_count, one_count = self._count(strs[i - 1])

            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zero_count and k >= one_count:
                        dp[i][j][k] = max(
                            dp[i - 1][j][k],
                            dp[i - 1][j - zero_count][k - one_count] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[length][m][n]

    def _count(self, s):
        zero_count = 0
        one_count = 0

        for c in s:
            if c == '0':
                zero_count += 1
            elif c == '1':
                one_count += 1

        return zero_count, one_count
