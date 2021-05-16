from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[m - 1][n - 1]

        while low < high:
            middle = low + (high - low) // 2
            count = self._get_count_less_than_target(matrix, m, n, middle)

            if count < k:
                low = middle + 1
            else:
                high = middle

        return low

    def _get_count_less_than_target(self, matirx, m, n, middle):
        count = 0
        j = n - 1

        for i in range(m):
            while j >= 0 and matirx[i][j] > middle:
                j -= 1

            count += j + 1

        return count
