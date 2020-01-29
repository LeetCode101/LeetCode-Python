from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        length = len(prices)
        profits = [[0 for _ in range(2)] for _ in range(length)]
        profits[0][0] = 0
        profits[0][1] = -prices[0]

        for i in range(1, length):
            profits[i][0] = \
                max(profits[i - 1][0], profits[i - 1][1] + prices[i] - fee)
            profits[i][1] = \
                max(profits[i - 1][1], profits[i - 1][0] - prices[i])

        return profits[-1][0]
