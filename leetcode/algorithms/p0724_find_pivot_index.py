from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        pivot = 0
        left_sum, all_sum = 0, sum(nums)

        while pivot < len(nums):
            if all_sum - nums[pivot] - left_sum == left_sum:
                return pivot
            else:
                left_sum += nums[pivot]
                pivot += 1

        return -1
