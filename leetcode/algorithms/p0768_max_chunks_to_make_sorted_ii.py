from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        right_min = [-1] * n
        right_min[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i])

        max_so_far = arr[0]

        for i in range(n - 1):
            max_so_far = max(max_so_far, arr[i])

            if max_so_far <= right_min[i + 1]:
                count += 1

        return count + 1
