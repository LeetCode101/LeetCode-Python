import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            middle = left + (right - left) // 2
            current_sum = self._sum(nums, middle)

            if current_sum > threshold:
                left = middle + 1
            else:
                right = middle

        return left

    def _sum(self, nums, divisor):
        return sum([math.ceil(x / divisor) for x in nums])
