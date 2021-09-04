from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        prev_max = -1

        for i, n in enumerate(arr):
            prev_max = max(prev_max, n)

            if prev_max == i:
                count += 1

        return count
