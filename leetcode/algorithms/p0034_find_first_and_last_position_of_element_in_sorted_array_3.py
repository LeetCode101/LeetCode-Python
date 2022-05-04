from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        return [self._find_first(nums, target), self._find_last(nums, target)]

    def _find_first(self, nums, target):
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2

            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle

        return low if nums[low] == target else -1

    def _find_last(self, nums, target):
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2 + 1

            if nums[middle] <= target:
                low = middle
            else:
                high = middle - 1

        return low if nums[low] == target else - 1
