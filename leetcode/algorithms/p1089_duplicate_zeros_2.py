from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = len(list(filter(lambda x: x == 0, arr)))
        length = len(arr)

        for i in range(length - 1, -1, -1):
            if arr[i] != 0:
                if i + zeros < length:
                    arr[i + zeros] = arr[i]
            else:
                if i + 1 + zeros - 1 < length:
                    arr[i + 1 + zeros - 1] = 0

                if i + zeros - 1 < length:
                    arr[i + zeros - 1] = 0

                zeros -= 1
