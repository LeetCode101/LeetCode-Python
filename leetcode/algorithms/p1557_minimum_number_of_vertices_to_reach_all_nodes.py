import collections
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) \
            -> List[int]:
        visited = set()
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            visited.add(b)

        result = []

        for i in range(n):
            if i not in visited:
                result.append(i)

        return result
