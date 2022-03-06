import math
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            middle = left + (right - left) // 2
            current_operations = self._count_operations(nums, middle)

            if current_operations > maxOperations:
                left = middle + 1
            else:
                right = middle

        return left

    def _count_operations(self, nums, penalty):
        return sum([math.ceil(x / penalty) - 1 for x in nums])
