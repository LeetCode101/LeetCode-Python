import bisect
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left = bisect.bisect_left(sorted_nums, target)
        right = bisect.bisect_right(sorted_nums, target)

        return list(range(left, right))
