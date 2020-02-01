import math
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        m, n = len(matrix), len(matrix[0])

        for i in range(math.ceil(min(m, n) / 2)):
            for j in range(i, n - i):
                result.append(matrix[i][j])

            for j in range(i + 1, m - i):
                result.append(matrix[j][n - i - 1])

            if i != m - i - 1:
                for j in range(n - i - 2, i - 1, -1):
                    result.append(matrix[m - i - 1][j])

            if i != n - i - 1:
                for j in range(m - i - 2, i, -1):
                    result.append(matrix[j][i])

        return result
