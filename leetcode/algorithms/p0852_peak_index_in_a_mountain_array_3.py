from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            middle = low + (high - low) // 2

            if arr[middle] < arr[middle + 1]:
                low = middle + 1
            else:
                high = middle

        return low
