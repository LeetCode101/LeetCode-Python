from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2

            if nums[middle] > nums[high]:
                low = middle + 1
            elif nums[middle] < nums[high]:
                high = middle
            else:
                high -= 1

        return nums[high]
