from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if i == len(arr) - 1:
                    return False

                continue

            if i == 1:
                return False

            for j in range(i, len(arr)):
                if arr[j] >= arr[j - 1]:
                    return False

            break

        return len(arr) >= 3
