from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right = 0, max(inventory)
        bound = -1
        mod = 1000000007

        while left < right:
            middle = left + (right - left) // 2
            total = sum(x - middle for x in inventory if x >= middle)

            if total <= orders:
                bound = middle
                right = middle
            else:
                left = middle + 1

        rest = orders - sum(x - bound for x in inventory if x >= bound)
        profit = rest * bound

        for x in inventory:
            if x < bound:
                continue

            profit = (profit + self._range_sum(bound + 1, x)) % mod

        return profit

    def _range_sum(self, x, y):
        return y * (1 + y) // 2 - (x - 1) * (1 + x - 1) // 2
