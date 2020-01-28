from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        count = sum(len(x) for x in triangle)
        sums = [0] * count
        sums[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                index = i * (i + 1) // 2 + j
                sums[index] = triangle[i][j]

                if j == 0:
                    sums[index] += sums[index - i]
                elif j - 1 >= 0 and j <= len(triangle[i - 1]) - 1:
                    sums[index] += min(sums[index - i - 1], sums[index - i])
                else:
                    sums[index] += sums[index - i - 1]

        return min(sums[count - len(triangle[-1]):])
