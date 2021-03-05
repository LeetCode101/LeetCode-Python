import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) \
            -> float:
        m, n = len(nums1), len(nums2)
        k1, k2 = (m + n + 1) // 2, (m + n + 2) // 2

        return (self._find_kth(nums1, 0, nums2, 0, k1) +
                self._find_kth(nums1, 0, nums2, 0, k2)) / 2

    def _find_kth(self, nums1: List[int], i: int,
                  nums2: List[int], j: int, k: int) -> int:
        if i >= len(nums1):
            return nums2[j + k - 1]

        if j >= len(nums2):
            return nums1[i + k - 1]

        if k == 1:
            return min(nums1[i], nums2[j])

        middle_value1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) \
            else sys.maxsize
        middle_value2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) \
            else sys.maxsize

        if middle_value1 < middle_value2:
            return self._find_kth(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self._find_kth(nums1, i, nums2, j + k // 2, k - k // 2)
