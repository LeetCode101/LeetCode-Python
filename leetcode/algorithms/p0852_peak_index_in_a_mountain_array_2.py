from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0

        while low + 1 < len(arr) - 1:
            if arr[low] >= arr[low + 1]:
                break

            low += 1

        return low
