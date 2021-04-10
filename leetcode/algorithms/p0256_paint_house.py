from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        last_red, last_green, last_blue = costs[0][0], costs[0][1], costs[0][2]

        for i in range(1, len(costs)):
            current_red = min(last_green, last_blue) + costs[i][0]
            current_green = min(last_red, last_blue) + costs[i][1]
            current_blue = min(last_red, last_green) + costs[i][2]
            last_red, last_green, last_blue = \
                current_red, current_green, current_blue

        return min(last_red, last_green, last_blue)
