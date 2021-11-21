from typing import List


# Time Limit Exceeded!
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = points[0][i]

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = max([dp[i - 1][k] + points[i][j] - abs(j - k)
                                for k in range(n)])

        return max(dp[-1])
