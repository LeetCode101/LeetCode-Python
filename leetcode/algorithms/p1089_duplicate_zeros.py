from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, length = 0, len(arr)

        while i < length:
            if arr[i] == 0 and i + 1 < length:
                self.shift(arr, i + 1)
                arr[i + 1] = 0
                i += 1

            i += 1

    def shift(self, arr: List[int], i: int) -> None:
        for j in range(len(arr) - 1, i, -1):
            arr[j] = arr[j - 1]
