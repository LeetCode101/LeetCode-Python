from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_sum_so_far = nums[0]

        for i in range(1, len(nums)):
            max_sum_so_far = max(max_sum_so_far + nums[i], nums[i])
            max_sum = max(max_sum_so_far, max_sum)

        return max_sum
