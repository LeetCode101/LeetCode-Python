from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        cost_so_far = [costs[0][0], costs[0][1], costs[0][2]]

        for i in range(1, len(costs)):
            red_cost = min(cost_so_far[1], cost_so_far[2]) + costs[i][0]
            green_cost = min(cost_so_far[0], cost_so_far[2]) + costs[i][1]
            blue_cost = min(cost_so_far[0], cost_so_far[1]) + costs[i][2]
            cost_so_far = [red_cost, green_cost, blue_cost]

        return min(cost_so_far)
