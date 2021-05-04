from typing import List


# Time Limit Exceeded!
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        result = []
        row, column = len(mat), len(mat[0])

        for i in range(row + column - 1):
            for p in range(i + 1):
                m, n = p, i - p

                if i & 1 == 0:
                    m, n = n, m

                if m >= row or n >= column:
                    continue

                result.append(mat[m][n])

        return result
