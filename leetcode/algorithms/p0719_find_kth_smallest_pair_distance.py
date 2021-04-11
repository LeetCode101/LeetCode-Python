from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            middle = low + (high - low) // 2

            if self._has_more_than_k_pairs(nums, k, middle):
                high = middle
            else:
                low = middle + 1

        return low

    def _has_more_than_k_pairs(self, nums: List[int],
                               k: int, middle_distance: int) -> bool:
        count = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > middle_distance:
                left += 1

            count += right - left

            if count >= k:
                return True

        return False
