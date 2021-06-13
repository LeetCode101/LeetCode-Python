from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        digits = [0] * (len(nums) + 1)

        for n in nums:
            digits[n] = 1

        for i, n in enumerate(digits):
            if n == 0:
                return i
