import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = sorted(nums1)
        sum_diff = 0
        n = len(nums1)
        mod = 1000000007
        max_replace = 0

        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            sum_diff += diff
            j = bisect.bisect_left(sorted_nums1, nums2[i])

            if j < n:
                gap = sorted_nums1[j] - nums2[i]
                max_replace = max(max_replace, diff - gap)

            if j > 0:
                gap = nums2[i] - sorted_nums1[j - 1]
                max_replace = max(max_replace, diff - gap)

        return (sum_diff - max_replace) % mod
