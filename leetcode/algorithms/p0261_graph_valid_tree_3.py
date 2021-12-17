from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbours = {i: [] for i in range(n)}

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        self._dfs(neighbours, 0)

        return len(edges) == n - 1 and not neighbours

    def _dfs(self, neighbours, node):
        for neighbour in neighbours.pop(node, []):
            self._dfs(neighbours, neighbour)
