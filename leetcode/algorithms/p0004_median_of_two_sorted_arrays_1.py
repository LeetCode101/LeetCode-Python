from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) \
            -> float:
        n = len(nums1) + len(nums2)
        middle = n // 2
        sorted_list = sorted(nums1 + nums2)

        return sorted_list[middle] if n % 2 == 1 else \
            (sorted_list[middle - 1] + sorted_list[middle]) / 2
