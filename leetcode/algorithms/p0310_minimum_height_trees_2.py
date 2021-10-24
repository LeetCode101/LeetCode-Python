import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [n - 1]

        neighbours = collections.defaultdict(list)

        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])

        queue = collections.deque()

        for node, neighbour in neighbours.items():
            if len(neighbour) == 1:
                queue.append(node)

        while queue and n > 2:
            size = len(queue)
            n -= size

            for _ in range(size):
                node = queue.popleft()
                neighbour = neighbours[node].pop()
                neighbours[neighbour].remove(node)

                if len(neighbours[neighbour]) == 1:
                    queue.append(neighbour)

        return list(queue)
