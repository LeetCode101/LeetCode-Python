from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2
            value = nums[middle]

            if value > target:
                high = middle - 1
            elif value < target:
                low = middle + 1
            else:
                return middle

        return -1
