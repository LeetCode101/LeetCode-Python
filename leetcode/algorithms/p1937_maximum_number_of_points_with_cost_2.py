from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        for i in range(1, m):
            left = [points[i - 1][0]] * n

            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, points[i - 1][j])

            right = [points[i - 1][n - 1]] * n

            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, points[i - 1][j])

            for j in range(n):
                points[i][j] += max(left[j], right[j])

        return max(points[-1])
