from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, column = 0, n - 1

        while row < m and column >= 0:
            if matrix[row][column] == target:
                return True
            if matrix[row][column] < target:
                row += 1
            else:
                column -= 1

        return False
