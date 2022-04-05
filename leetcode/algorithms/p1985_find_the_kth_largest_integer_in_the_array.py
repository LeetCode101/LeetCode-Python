from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        low, high = 0, len(nums) - 1

        while low <= high:
            p = self._partition(nums, low, high)

            if p == k - 1:
                return nums[p]
            elif p > k - 1:
                high = p - 1
            else:
                low = p + 1

    def _partition(self, nums: List[str], low: int, high: int):
        pivot = (low + high) // 2
        pivot_value = int(nums[pivot])
        nums[pivot], nums[high] = nums[high], nums[pivot]
        p = low

        for i in range(low, high):
            if int(nums[i]) >= pivot_value:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[high], nums[p] = nums[p], nums[high]

        return p