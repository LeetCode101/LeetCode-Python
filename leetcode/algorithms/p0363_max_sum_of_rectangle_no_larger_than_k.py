import bisect
import sys
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        row, column = len(matrix), len(matrix[0])
        max_sum = -sys.maxsize

        for i in range(row):
            column_sum = [0] * column

            for j in range(i, row):
                for c in range(column):
                    column_sum[c] += matrix[j][c]

                max_sum = max(max_sum, self._max_sum(column_sum, k))

        return max_sum

    def _max_sum(self, column_sum, k):
        max_sum = -sys.maxsize
        sum_so_far = 0
        prefix_sums = [0]

        for n in column_sum:
            sum_so_far += n
            i = bisect.bisect_left(prefix_sums, sum_so_far - k)

            if 0 <= i < len(prefix_sums):
                max_sum = max(max_sum, sum_so_far - prefix_sums[i])

            bisect.insort(prefix_sums, sum_so_far)

        return max_sum
