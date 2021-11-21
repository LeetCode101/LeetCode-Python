from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [points[0][i] for i in range(n)]

        for i in range(1, m):
            left = [dp[0]] * n

            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, dp[j])

            right = [dp[n - 1]] * n

            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, dp[j])

            for j in range(n):
                dp[j] = max(left[j], right[j]) + points[i][j]

        return max(dp)
