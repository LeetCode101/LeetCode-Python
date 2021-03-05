from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        step = k % len(nums)
        length = len(nums)

        self._reverse(nums, 0, length - 1)
        self._reverse(nums, 0, step - 1)
        self._reverse(nums, step, length - 1)

    def _reverse(self, nums: List[int], low: int, high: int) -> None:
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
