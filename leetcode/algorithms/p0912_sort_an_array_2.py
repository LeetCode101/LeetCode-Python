from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._quick_sort(nums, 0, len(nums) - 1)

        return nums

    def _quick_sort(self, nums, low, high):
        if low >= high:
            return

        pivot = self._partition(nums, low, high)

        self._quick_sort(nums, low, pivot - 1)
        self._quick_sort(nums, pivot, high)

    def _partition(self, nums, low, high):
        middle = low + (high - low) // 2
        pivot = nums[middle]

        while low <= high:
            while nums[low] < pivot:
                low += 1

            while nums[high] > pivot:
                high -= 1

            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        return low
