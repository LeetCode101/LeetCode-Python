import sys
from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dp = [sys.maxsize] * len(arr)
        sum_so_far, best_so_far = 0, sys.maxsize
        min_length, start = sys.maxsize, 0

        for i, n in enumerate(arr):
            sum_so_far += n

            while sum_so_far > target:
                sum_so_far -= arr[start]
                start += 1

            if sum_so_far == target:
                current_window_length = i - start + 1

                if start > 0 and dp[start - 1] != sys.maxsize:
                    min_length = min(min_length,
                                     dp[start - 1] + current_window_length)

                best_so_far = min(best_so_far, current_window_length)

            dp[i] = best_so_far

        return min_length if min_length != sys.maxsize else -1
