from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, length = 0, len(arr)

        while i < length:
            if arr[i] == 0 and i + 1 < length:
                i += 1
                self._shift(arr, i)
                arr[i] = 0

            i += 1

    def _shift(self, arr: List[int], i: int) -> None:
        for j in range(len(arr) - 1, i, -1):
            arr[j] = arr[j - 1]
