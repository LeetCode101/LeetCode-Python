import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)

        while left < right:
            middle = left + (right - left) // 2
            current_sum = sum([math.ceil(x / middle) for x in quantities])

            if current_sum > n:
                left = middle + 1
            else:
                right = middle

        return left
