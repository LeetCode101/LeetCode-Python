from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left_sum, all_sum = 0, sum(nums)

        for i, n in enumerate(nums):
            if all_sum - n - left_sum == left_sum:
                return i
            else:
                left_sum += n

        return -1
