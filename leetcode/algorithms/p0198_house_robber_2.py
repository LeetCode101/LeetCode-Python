from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return max(nums)

        prev_prev = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            prev, prev_prev = max(prev_prev + nums[i], prev), prev

        return prev
