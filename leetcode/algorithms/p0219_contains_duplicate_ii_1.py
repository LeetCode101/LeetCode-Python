from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}

        for i, n in enumerate(nums):
            if n in mapping and abs(i - mapping[n]) <= k:
                return True

            mapping[n] = i

        return False
