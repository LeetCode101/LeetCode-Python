from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        self.rotate_internal(nums, k, 0, len(nums) - 1)

    def rotate_internal(self, nums: List[int], k: int, low: int, high: int) \
            -> None:
        if low >= high or k == 0:
            return

        size = high - low + 1
        step = k % size

        for i in range(step):
            nums[low + i], nums[high - step + 1 + i] = \
                nums[high - step + 1 + i], nums[low + i]

        self.rotate_internal(nums, step, low + step, high)
