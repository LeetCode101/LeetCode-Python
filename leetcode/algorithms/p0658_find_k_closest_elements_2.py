from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k

        while low < high:
            middle = low + (high - low) // 2

            if x - arr[middle] > arr[middle + k] - x:
                low = middle + 1
            else:
                high = middle

        return arr[low:low + k]
