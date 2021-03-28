from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - 1

        while high - low >= k:
            if abs(arr[low] - x) > abs(arr[high] - x):
                low += 1
            else:
                high -= 1

        return arr[low:high + 1]
