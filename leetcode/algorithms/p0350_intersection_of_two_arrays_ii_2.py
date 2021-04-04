from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        result = []
        i = j = 0

        while i < len(sorted1) and j < len(sorted2):
            if sorted1[i] < sorted2[j]:
                i += 1
            elif sorted1[i] > sorted2[j]:
                j += 1
            else:
                result.append(sorted1[i])
                i += 1
                j += 1

        return result
