import collections
import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        sum_so_far = 0
        sum_mapping = collections.defaultdict(list)
        sum_mapping[0] = [-1]
        intervals = []
        min_length = sys.maxsize

        for i, n in enumerate(arr):
            sum_so_far += n

            if sum_so_far - target in sum_mapping:
                for j in sum_mapping[sum_so_far - target]:
                    intervals.append((j + 1, i))

            sum_mapping[sum_so_far].append(i)

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals[i][1] >= intervals[j][0]:
                    continue

                current_length = intervals[i][1] - intervals[i][0] + 1 \
                    + intervals[j][1] - intervals[j][0] + 1
                min_length = min(min_length, current_length)

        return -1 if min_length == sys.maxsize else min_length
