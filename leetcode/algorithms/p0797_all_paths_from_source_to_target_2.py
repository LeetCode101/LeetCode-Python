from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        n = len(graph) - 1
        paths = []
        queue = deque([(0, [0])])

        while queue:
            node, path = queue.popleft()

            if node == n:
                paths.append(path)
            else:
                for i in graph[node]:
                    queue.append((i, path + [i]))

        return paths
