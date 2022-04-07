import bisect
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        if left == len(nums) or nums[left] != target:
            return False

        return right - left > len(nums) / 2
