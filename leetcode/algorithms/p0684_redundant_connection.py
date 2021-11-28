from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        roots = [0] * (len(edges) + 1)

        for x, y in edges:
            root_x = self._get_root(roots, x)
            root_y = self._get_root(roots, y)

            if root_x == root_y and root_x != 0:
                return [x, y]

            roots[root_x] = root_y

        return []

    def _get_root(self, roots, x):
        while roots[x] != 0:
            x = roots[x]

        return x
