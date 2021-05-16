import sys
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[m - 1][n - 1]

        while low <= high:
            middle = low + (high - low) // 2
            count, max_num = self._get_count_less_than_target(
                matrix, m, n, middle)

            if count < k:
                low = middle + 1
            elif count == k:
                return max_num
            else:
                high = middle - 1

        return low

    def _get_count_less_than_target(self, matirx, m, n, middle):
        count = 0
        max_num = -sys.maxsize
        j = n - 1

        for i in range(m):
            while j >= 0 and matirx[i][j] > middle:
                j -= 1

            if j >= 0:
                max_num = max(max_num, matirx[i][j])

            count += j + 1

        return count, max_num
