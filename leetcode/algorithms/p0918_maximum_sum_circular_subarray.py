from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, max_sum, max_so_far, min_sum, min_so_far = 0, nums[0], 0, nums[0], 0

        for n in nums:
            max_so_far = max(max_so_far + n, n)
            max_sum = max(max_sum, max_so_far)
            min_so_far = min(min_so_far + n, n)
            min_sum = min(min_sum, min_so_far)
            total +=n

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
