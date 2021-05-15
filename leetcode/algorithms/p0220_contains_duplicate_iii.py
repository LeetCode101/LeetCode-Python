import bisect
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) \
            -> bool:
        bst = []

        for i, n in enumerate(nums):
            if i > k:
                del bst[bisect.bisect_left(bst, nums[i - k - 1])]

            pos1 = bisect.bisect_left(bst, nums[i] - t)
            pos2 = bisect.bisect_right(bst, nums[i] + t)

            if pos1 != pos2:
                return True

            bisect.insort(bst, n)

        return False
