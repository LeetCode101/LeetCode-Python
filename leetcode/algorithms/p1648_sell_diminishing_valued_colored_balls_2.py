from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        left, right = 0, max(inventory)
        bound = -1
        mod = 1000000007

        while left <= right:
            middle = left + (right - left) // 2
            total = sum(x - middle for x in inventory if x >= middle)

            if total <= orders:
                bound = middle
                right = middle - 1
            else:
                left = middle + 1

        rest = orders - sum(x - bound for x in inventory if x >= bound)
        profit = 0

        for x in inventory:
            if x < bound:
                continue

            if rest > 0:
                profit = (profit + self._range_sum(bound, x)) % mod
                rest -= 1
            else:
                profit = (profit + self._range_sum(bound + 1, x)) % mod

        return profit

    def _range_sum(self, x, y):
        return (x + y) * (y - x + 1) // 2

