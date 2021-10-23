from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        min_length = 0
        low, high = 0, 0
        sum_so_far = nums[0]

        while high < len(nums):
            if sum_so_far >= target:
                current_length = high - low + 1
                min_length = min(min_length, current_length) \
                    if min_length != 0 else current_length
                sum_so_far -= nums[low]
                low += 1
            else:
                high += 1
                sum_so_far += nums[high] if high < len(nums) else 0

        return min_length
