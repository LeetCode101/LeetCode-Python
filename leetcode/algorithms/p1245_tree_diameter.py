import collections
from typing import List


class Solution:
    def __init__(self):
        self.max_length = 0

    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self._dfs(graph, 0, -1)

        return self.max_length

    def _dfs(self, graph, node, parent):
        max1, max2 = 0, 0

        for child in graph[node]:
            if child == parent:
                continue

            depth = self._dfs(graph, child, node)

            if depth > max1:
                max1, max2 = depth, max1
            elif depth > max2:
                max2 = depth

        self.max_length = max(self.max_length, max1 + max2)

        return max1 + 1
