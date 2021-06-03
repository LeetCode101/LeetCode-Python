from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self._merge_sort(nums, 0, len(nums) - 1)

        return nums

    def _merge_sort(self, nums, low, high):
        if low >= high:
            return

        middle = low + (high - low) // 2

        self._merge_sort(nums, low, middle)
        self._merge_sort(nums, middle + 1, high)
        self._merge(nums, low, middle, high)

    def _merge(self, nums, low, middle, high):
        if nums[middle] <= nums[middle + 1]:
            return

        left = low
        right = middle + 1
        merged = []

        while left <= middle or right <= high:
            if left <= middle and right <= high:
                if nums[left] <= nums[right]:
                    merged.append(nums[left])
                    left += 1
                else:
                    merged.append(nums[right])
                    right += 1
            elif left <= middle:
                merged.append(nums[left])
                left += 1
            else:
                merged.append(nums[right])
                right += 1

        for i in range(low, high + 1):
            nums[i] = merged[i - low]
