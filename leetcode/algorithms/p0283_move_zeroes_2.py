from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail += 1
