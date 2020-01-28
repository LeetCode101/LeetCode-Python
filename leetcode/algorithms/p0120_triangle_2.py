from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sums = [[0] * len(t) for t in triangle]
        sums[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                sums[i][j] = triangle[i][j]

                if j == 0:
                    sums[i][j] += sums[i - 1][0]
                elif j - 1 >= 0 and j <= len(triangle[i - 1]) - 1:
                    sums[i][j] += min(sums[i - 1][j - 1], sums[i - 1][j])
                else:
                    sums[i][j] += sums[i - 1][j - 1]

        return min(sums[-1])
