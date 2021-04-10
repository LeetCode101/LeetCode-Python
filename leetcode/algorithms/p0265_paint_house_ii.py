import sys
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        k = len(costs[0])
        cost_so_far = [x for x in costs[0]]

        for i in range(1, len(costs)):
            current_cost = [0] * k

            for j in range(k):
                current_cost[j] = self._min_cost(cost_so_far, j) + costs[i][j]

            cost_so_far = current_cost

        return min(cost_so_far)

    def _min_cost(self, cost_so_far, i):
        min_cost = sys.maxsize

        for j, cost in enumerate(cost_so_far):
            if j != i and min_cost > cost:
                min_cost = cost

        return min_cost
