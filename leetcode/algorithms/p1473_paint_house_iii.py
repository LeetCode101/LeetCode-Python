import functools
import sys
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]],
                m: int, n: int, target: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, neighbor_count, prev_color):
            if i == m and neighbor_count == target:
                return 0

            if i >= m or neighbor_count > target:
                return sys.maxsize

            current_min_cost = sys.maxsize

            if houses[i]:
                current_min_cost = dfs(
                    i + 1, neighbor_count + (houses[i] != prev_color),
                    houses[i])
            else:
                for color in range(1, n + 1):
                    next_house_cost = dfs(
                        i + 1, neighbor_count + (color != prev_color), color)
                    current_min_cost = min(
                        current_min_cost, cost[i][color - 1] + next_house_cost)

            return current_min_cost

        min_cost = dfs(0, 0, None)

        return min_cost if min_cost != sys.maxsize else -1
