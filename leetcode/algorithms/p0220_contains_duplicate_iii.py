import bisect
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) \
            -> bool:
        bst = []

        for i, n in enumerate(nums):
            if i > k:
                del bst[bisect.bisect_left(bst, nums[i - k - 1])]

            left = bisect.bisect_left(bst, nums[i] - t)
            right = bisect.bisect_right(bst, nums[i] + t)

            if left != right:
                return True

            bisect.insort(bst, n)

        return False
