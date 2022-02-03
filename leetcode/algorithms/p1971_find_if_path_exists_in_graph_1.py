import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]],
                  source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        return self._dfs(graph, source, destination, set())

    def _dfs(self, graph, source, destination, visited):
        if source == destination:
            return True

        if source in visited:
            return False

        visited.add(source)

        for neighbour in graph[source]:
            if self._dfs(graph, neighbour, destination, visited):
                return True

        return False
