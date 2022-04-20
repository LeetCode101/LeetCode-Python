from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        total_cost = 0
        max_cost = 0

        for i in range(n):
            if i > 0 and colors[i] != colors[i - 1]:
                max_cost = 0

            total_cost += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])

        return total_cost
