from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = set()

        for i, n in enumerate(nums):
            if i > k:
                numbers.remove(nums[i - k - 1])

            if n in numbers:
                return True

            numbers.add(n)

        return False
