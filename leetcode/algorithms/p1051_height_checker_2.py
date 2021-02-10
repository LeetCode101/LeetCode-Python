import collections
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = collections.Counter(heights)
        current_height, count = 1, 0

        for height in heights:
            while counts[current_height] == 0:
                current_height += 1

            if current_height != height:
                count += 1

            counts[current_height] -= 1

        return count
