from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        top, length = -1, len(arr)

        for i in range(1, length):
            if arr[i] > arr[i - 1]:
                continue
            else:
                top = i - 1
                break

        if top <= 0:
            return False

        for i in range(top + 1, length):
            if arr[i] >= arr[i - 1]:
                return False

        return top < length - 1
