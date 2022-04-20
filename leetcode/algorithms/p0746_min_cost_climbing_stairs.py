from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, prev_prev = 0, 0

        for i in range(2, len(cost) + 1):
            prev, prev_prev = min(prev + cost[i - 1],
                                  prev_prev + cost[i - 2]), prev

        return prev
