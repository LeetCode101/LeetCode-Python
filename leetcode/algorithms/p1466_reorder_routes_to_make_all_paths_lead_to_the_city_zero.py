import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        direction = [[False] * n for _ in range(n)]

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            direction[a][b] = True

        queue = collections.deque([0])
        visited = {0}
        count = 0

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    if direction[node][neighbour]:
                        count += 1

                    visited.add(neighbour)
                    queue.append(neighbour)

        return count