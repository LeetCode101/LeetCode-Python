from random import shuffle
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        shuffle(nums)
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = self._partition(nums, lo, hi)
            if mid == k - 1:
                return str(nums[mid])
            elif mid < k - 1:
                lo = mid + 1
            else:
                hi = mid - 1

    def _partition(self, nums, low, high):
        i, j = low, high - 1
        pivot = low + (high - low) // 2
        pivot_value = int(nums[pivot])
        nums[pivot], nums[high] = nums[high], nums[pivot]

        while i <= j:
            if int(nums[i]) > pivot_value:
                i += 1
            elif int(nums[j]) < pivot_value:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        nums[i], nums[high] = nums[high], nums[i]

        return i
