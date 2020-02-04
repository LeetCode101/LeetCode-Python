from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2

            if nums[middle] > nums[high]:
                low = middle + 1
            else:
                high = middle

        return nums[high]
