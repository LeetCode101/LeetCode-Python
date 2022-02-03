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
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            if node in visited:
                continue

            visited.add(node)

            for neighbour in graph[node]:
                stack.append(neighbour)

        return False
