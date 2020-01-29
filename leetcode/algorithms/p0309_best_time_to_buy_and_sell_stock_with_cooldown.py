from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        profits = [[[0 for _ in range(2)] for _ in range(2)]
                   for _ in range(length)]
        profits[0][0][0], profits[0][0][1] = 0, -prices[0]
        profits[0][1][0], profits[0][1][1] = 0, 0

        for i in range(1, length):
            profits[i][0][0] = max(profits[i - 1][0][0], profits[i - 1][1][0])
            profits[i][0][1] = \
                max(profits[i - 1][0][1], profits[i - 1][0][0] - prices[i])
            profits[i][1][0] = profits[i - 1][0][1] + prices[i]

        return max(profits[-1][0][0], profits[-1][1][0])
