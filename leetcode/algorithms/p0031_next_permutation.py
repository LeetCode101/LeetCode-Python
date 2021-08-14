from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1

        while i - 1 >= 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.sort()

            return

        j = i

        while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
            j += 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
