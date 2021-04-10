import functools
import sys
from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]],
                m: int, n: int, target: int) -> int:
        min_cost = self._dfs(0, 0, None, houses, cost, m, n, target)

        return min_cost if min_cost != sys.maxsize else -1

    @functools.lru_cache
    def _dfs(self, i, k, p, houses: List[int], cost: List[List[int]], m: int, n: int, target: int):
        if i == m and k == target:
            return 0

        if i >= m or k > target:
            return sys.maxsize

        min_cost = sys.maxsize

        if houses[i]:
            min_cost = min(min_cost, self._dfs(i + 1, k + (houses[i] != p), houses[i], houses, cost, m, n, target))
        else:
            for color in range(1, n + 1):
                min_cost = min(min_cost, cost[i][color - 1] + self._dfs(i + 1, k + (color != p), color, houses, cost, m, n, target))

        return min_cost
