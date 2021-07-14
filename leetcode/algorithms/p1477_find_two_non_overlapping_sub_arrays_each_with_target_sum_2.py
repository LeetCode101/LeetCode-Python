import collections
import sys
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sum_so_far = 0
        sum_mapping = collections.defaultdict(int)
        sum_mapping[0] = -1
        min_left_size = sys.maxsize
        min_length = sys.maxsize

        for i, n in enumerate(arr):
            sum_so_far += n
            sum_mapping[sum_so_far] = i

        sum_so_far = 0

        for i, n in enumerate(arr):
            sum_so_far += n

            if sum_so_far - target in sum_mapping:
                min_left_size = min(
                    min_left_size, i - sum_mapping[sum_so_far - target])

            if sum_so_far + target in sum_mapping \
                    and min_left_size != sys.maxsize:
                current_length = sum_mapping[sum_so_far + target] - i \
                                 + min_left_size
                min_length = min(min_length, current_length)

        return -1 if min_length == sys.maxsize else min_length
