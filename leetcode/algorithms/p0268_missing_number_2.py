from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        digits = set(nums)
        all_digits = set([i for i in range(len(nums) + 1)])

        for n in all_digits:
            if n not in digits:
                return n
