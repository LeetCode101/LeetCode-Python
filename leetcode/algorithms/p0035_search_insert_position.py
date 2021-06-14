from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            middle = low + (high - low) // 2

            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle

        return low
