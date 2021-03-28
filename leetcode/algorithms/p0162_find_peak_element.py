from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            larger_than_left = (i - 1 >= 0 and nums[i - 1] < nums[i]) or i == 0
            larger_than_right = (i + 1 < len(nums) and nums[i + 1] < nums[i]) \
                or i + 1 == len(nums)

            if larger_than_left and larger_than_right:
                return i

        return -1
