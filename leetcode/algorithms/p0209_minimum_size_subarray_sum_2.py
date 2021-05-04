from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 0
        sums = [0] * len(nums)

        for i, n in enumerate(nums):
            sums[i] = sums[i - 1] + n if i != 0 else n

        left = 0

        for right, n in enumerate(sums):
            if n >= target:
                left = self._find_left(left, right, sums, n - target)
                current_length = right - left + 1
                min_length = min(min_length, current_length) \
                    if min_length != 0 else current_length

        return min_length

    def _find_left(self, left, right, sums, target):
        while left < right:
            middle = left + (right - left) // 2

            if sums[middle] <= target:
                left = middle + 1
            else:
                right = middle

        return left
