from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self._binary_search(nums, target, True)
        end = self._binary_search(nums, target, False)

        return [start, end]

    def _binary_search(self, nums, target, find_first):
        i = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            else:
                i = middle

                if find_first:
                    high = middle - 1
                else:
                    low = middle + 1

        return i
