from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        largest = len(arr)

        while largest != 0:
            i = self._find(arr, largest)

            self._flip(arr, i)
            self._flip(arr, largest - 1)

            result.append(i + 1)
            result.append(largest)

            largest -= 1

        return result

    def _find(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i

        return -1

    def _flip(self, arr, i):
        low, high = 0, i

        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
