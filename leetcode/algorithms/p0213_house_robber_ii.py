from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        return max(self._rob(nums, 0, len(nums) - 2),
                   self._rob(nums, 1, len(nums) - 1))

    def _rob(self, nums, start, end):
        prev_prev = nums[start]
        prev = max(nums[start], nums[start + 1])

        for i in range(start + 2, end + 1):
            prev, prev_prev = max(prev_prev + nums[i], prev), prev

        return prev
