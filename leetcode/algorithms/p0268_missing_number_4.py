from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i, n in enumerate(nums):
            result ^= i
            result ^= n

        return result
