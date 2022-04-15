from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) \
            -> List[int]:
        visited = set()

        for a, b in edges:
            visited.add(b)

        return [i for i in range(n) if i not in visited]
