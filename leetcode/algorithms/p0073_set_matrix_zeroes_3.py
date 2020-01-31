from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        is_first_row_zero = False
        is_first_column_zero = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_row_zero = True

                    if j == 0:
                        is_first_column_zero = True

                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_first_row_zero:
            for i in range(n):
                matrix[0][i] = 0

        if is_first_column_zero:
            for i in range(m):
                matrix[i][0] = 0
