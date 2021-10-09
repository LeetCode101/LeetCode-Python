from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        numbers = sorted(nums)

        for i in range(1, len(nums), 2):
            nums[i] = numbers[end]
            end -= 1

        for i in range(0, len(nums), 2):
            nums[i] = numbers[end]
            end -= 1
