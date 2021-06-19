import collections
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) \
            -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        count = 0

        for i in range(m):
            column_sum = [0] * n

            for j in range(i, m):
                mapping = collections.defaultdict(int)
                mapping[0] = 1
                sum_so_far = 0

                for column in range(n):
                    column_sum[column] += matrix[j][column]
                    sum_so_far += column_sum[column]
                    count += mapping[sum_so_far - target]
                    mapping[sum_so_far] += 1

        return count
