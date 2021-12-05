from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = list(range(len(edges) + 1))

        for x, y in edges:
            root_x = self._get_root(roots, x)
            root_y = self._get_root(roots, y)

            if root_x == root_y:
                return [x, y]

            roots[root_x] = root_y

        return []

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x
