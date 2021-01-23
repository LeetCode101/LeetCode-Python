from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        low, high = 0, len(arr) - 1

        while low + 1 < len(arr) - 1:
            if arr[low] >= arr[low + 1]:
                break

            low += 1

        while high - 1 >= 0:
            if arr[high - 1] <= arr[high]:
                break

            high -= 1

        return low == high and low != 0
