from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0

        while i < len(prices) - 1:
            diff = prices[i + 1] - prices[i]

            if diff > 0:
                profit += diff

            i += 1

        return profit
