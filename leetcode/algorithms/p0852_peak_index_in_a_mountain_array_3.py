from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if middle - 1 >= 0 and middle + 1 < len(arr):
                if arr[middle - 1] < arr[middle] > arr[middle + 1]:
                    return middle
                elif arr[middle - 1] >= arr[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            elif middle - 1 < 0:
                low = middle + 1
            else:
                high = middle - 1

        return -1
