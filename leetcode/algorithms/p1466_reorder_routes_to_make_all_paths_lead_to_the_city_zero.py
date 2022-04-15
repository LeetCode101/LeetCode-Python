import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        connection_set = set([(a, b) for a, b in connections])

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        queue = collections.deque([0])
        visited = {0}
        count = 0

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if (node, neighbour) in connection_set:
                        count += 1

                    visited.add(neighbour)
                    queue.append(neighbour)

        return count
