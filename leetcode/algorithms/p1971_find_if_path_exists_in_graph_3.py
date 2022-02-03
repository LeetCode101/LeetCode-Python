import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]],
                  source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        return self._bfs(graph, source, destination, set())

    def _bfs(self, graph, source, destination, visited):
        queue = collections.deque([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

        return False
