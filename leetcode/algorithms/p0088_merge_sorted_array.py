from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        tail = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1

            tail -= 1
