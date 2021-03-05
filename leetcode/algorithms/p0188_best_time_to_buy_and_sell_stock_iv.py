from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        if k >= len(prices) // 2:
            return self._max_profit_greedy(prices)

        profits = [[[0 for _ in range(2)] for _ in range(k + 1)]
                   for _ in range(len(prices))]

        for i in range(k + 1):
            profits[0][i][0] = 0
            profits[0][i][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k + 1):
                profits[i][j][0] = \
                    max(profits[i - 1][j][0],
                        profits[i - 1][j - 1][1] + prices[i]) \
                    if j >= 1 else profits[i - 1][j][0]
                profits[i][j][1] = \
                    max(profits[i - 1][j][1], profits[i - 1][j][0] - prices[i])

        return max([x[0] for x in profits[-1]])

    def _max_profit_greedy(self, prices: List[int]) -> int:
        profit = 0
        i = 0

        while i < len(prices) - 1:
            diff = prices[i + 1] - prices[i]

            if diff > 0:
                profit += diff

            i += 1

        return profit
