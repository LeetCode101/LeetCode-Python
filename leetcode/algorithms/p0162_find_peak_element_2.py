from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2

            if nums[middle] < nums[middle + 1]:
                low = middle + 1
            else:
                high = middle

        return low
