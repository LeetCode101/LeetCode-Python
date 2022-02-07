import collections
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i, x in enumerate(manager):
            if i != headID:
                graph[x].append(i)

        return self._dfs(graph, headID, informTime)

    def _dfs(self, graph, start, times):
        cost = 0

        for child in graph[start]:
            cost = max(cost, times[start] + self._dfs(graph, child, times))

        return cost
