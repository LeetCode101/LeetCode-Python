from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        row = self._binary_search([matrix[x][0] for x in range(m)], target)

        if matrix[row][0] == target:
            return True
        else:
            i = self._binary_search(matrix[row], target)

            return matrix[row][i] == target

    def _binary_search(self, numbers: List[int], target: int) -> int:
        low, high = 0, len(numbers) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if numbers[middle] == target:
                return middle
            elif numbers[middle] > target:
                high = middle - 1
            else:
                low = middle + 1

        return high
