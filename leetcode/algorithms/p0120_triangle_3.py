from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sums = [[0] * len(t) for t in triangle]

        for i, value in enumerate(triangle[-1]):
            sums[len(triangle) - 1][i] = value

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                sums[i][j] = triangle[i][j] + \
                             min(sums[i + 1][j], sums[i + 1][j + 1])

        return sums[0][0]
