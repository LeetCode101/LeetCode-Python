import collections
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbours = {i: [] for i in range(n)}

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        queue = collections.deque([0])

        while queue:
            for neighbour in neighbours.pop(queue.popleft(), []):
                queue.append(neighbour)

        return len(edges) == n - 1 and not neighbours
