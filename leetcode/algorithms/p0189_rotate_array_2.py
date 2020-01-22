from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        step = k % len(nums)
        length = len(nums)
        temp = [nums[i] for i in range(length - step)]

        for i in range(step):
            nums[i] = nums[length - step + i]

        for i in range(step, length):
            nums[i] = temp[i - step]
