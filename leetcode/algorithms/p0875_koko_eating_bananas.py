import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            middle = left + (right - left) // 2
            hours = sum([math.ceil(x / middle) for x in piles])

            if hours > h:
                left = middle + 1
            else:
                right = middle

        return left
