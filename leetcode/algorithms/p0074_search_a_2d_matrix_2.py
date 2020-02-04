from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            middle = low + (high - low) // 2
            row, column = middle // n, middle % n

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = middle - 1
            else:
                low = middle + 1

        return False
