from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        n = len(nums)

        while left < right:
            middle = left + (right - left) // 2

            if (middle & 1 == 1 and nums[middle - 1] == nums[middle]) or (
                    middle & 1 == 0 and middle + 1 < n and
                    nums[middle] == nums[middle + 1]):
                left = middle + 1
            else:
                right = middle

        return nums[left]
