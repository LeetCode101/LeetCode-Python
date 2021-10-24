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

        queue = []

        for node, neighbour in neighbours.items():
            if len(neighbour) == 1:
                queue.append(node)

        while queue and len(neighbours) > 2:
            nodes = []

            while queue:
                node = queue.pop()
                neighbour = neighbours[node][0]
                neighbours[neighbour].remove(node)

                if len(neighbours[neighbour]) == 1:
                    nodes.append(neighbour)

                del neighbours[node]

            queue = nodes[:]

        return list(neighbours.keys())
