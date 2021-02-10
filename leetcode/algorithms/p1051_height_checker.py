from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0

        for i, n in enumerate(heights):
            if n != sorted_heights[i]:
                count += 1

        return count
