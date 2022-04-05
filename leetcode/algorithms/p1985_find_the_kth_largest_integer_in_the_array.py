from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        low, high = 0, len(nums) - 1

        while low <= high:
            p = self._partition(nums, low, high)

            if p == k - 1:
                return str(nums[p])
            elif p < k - 1:
                low = p + 1
            else:
                high = p - 1

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
