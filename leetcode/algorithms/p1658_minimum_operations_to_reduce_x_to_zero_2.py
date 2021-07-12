from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x + sum(nums)

        if target == 0:
            return len(nums)

        if target < 0:
            return -1

        low, high = 0, 0
        total_sum = 0
        max_length = 0

        while high < len(nums):
            if total_sum < target:
                total_sum += nums[high]

            while total_sum >= target:
                if total_sum == target:
                    max_length = max(max_length, high - low + 1)

                total_sum -= nums[low]
                low += 1

            high += 1

        return -1 if max_length == 0 else len(nums) - max_length
