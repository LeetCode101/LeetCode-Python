from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        max_sum_so_far = nums[0]
        min_sum_so_far = nums[0]

        for i in range(1, len(nums)):
            max_sum_so_far = max(max_sum_so_far + nums[i], nums[i])
            min_sum_so_far = min(min_sum_so_far + nums[i], nums[i])
            max_sum = max(max_sum, max_sum_so_far)
            min_sum = min(min_sum, min_sum_so_far)

        return max(abs(max_sum), abs(min_sum))
