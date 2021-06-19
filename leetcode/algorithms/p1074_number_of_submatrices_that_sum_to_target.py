import collections
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) \
            -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        count = 0

        for up in range(m):
            nums = [0] * n

            for down in range(up, m):
                mapping = collections.defaultdict(int)
                mapping[0] = 1
                sum_so_far = 0

                for column in range(n):
                    nums[column] += matrix[down][column]
                    sum_so_far += nums[column]
                    count += mapping[sum_so_far - target]
                    mapping[sum_so_far] += 1

        return count
