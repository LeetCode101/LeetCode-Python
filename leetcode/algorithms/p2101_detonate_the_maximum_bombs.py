import collections
import math
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]
                distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

                if distance < r1 + r2:
                    graph[i].append(j)
                    graph[j].append(i)

        max_count = 0

        for i in range(n):
            count = self._count(graph, i, set())
            max_count = max(max_count, count)

        return max_count

    def _count(self, graph, start, visited):
        count = 0
        queue = collections.deque([start])

        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            count += 1
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

        return count
