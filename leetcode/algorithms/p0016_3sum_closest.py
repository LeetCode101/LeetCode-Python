import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = sys.maxsize

        for i in range(0, len(nums) - 2):
            k = target - nums[i]
            low, high = i + 1, len(nums) - 1

            while low < high:
                diff = nums[i] + nums[low] + nums[high] - target

                if abs(diff) < abs(min_diff):
                    min_diff = diff

                if nums[low] + nums[high] < k:
                    low += 1
                else:
                    high -= 1

        return target + min_diff
