import sys
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        min1 = min2 = 0
        index1 = -1
        k = len(costs[0])

        for i in range(len(costs)):
            current_min1 = sys.maxsize
            current_min2 = sys.maxsize
            current_index1 = -1

            for j in range(k):
                cost = costs[i][j] + (min1 if j != index1 else min2)

                if cost < current_min1:
                    current_min2 = current_min1
                    current_min1 = cost
                    current_index1 = j
                elif cost < current_min2:
                    current_min2 = cost

            min1 = current_min1
            min2 = current_min2
            index1 = current_index1

        return min1
