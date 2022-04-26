from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(abs(self._max_sum(nums)), abs(self._min_sum(nums)))

    def _max_sum(self, nums):
        max_sum = nums[0]
        sum_so_far = nums[0]

        for i in range(1, len(nums)):
            sum_so_far = max(sum_so_far + nums[i], nums[i])
            max_sum = max(max_sum, sum_so_far)

        return max_sum

    def _min_sum(self, nums):
        min_sum = nums[0]
        sum_so_far = nums[0]

        for i in range(1, len(nums)):
            sum_so_far = min(sum_so_far + nums[i], nums[i])
            min_sum = min(min_sum, sum_so_far)

        return min_sum
