from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0

        low, high = 1, max(ribbons)

        while low < high:
            middle = low + (high - low) // 2 + 1
            count = self._count_ribbons(ribbons, middle)

            if count >= k:
                low = middle
            else:
                high = middle - 1

        return low

    def _count_ribbons(self, ribbons, length):
        return sum([x // length for x in ribbons])
