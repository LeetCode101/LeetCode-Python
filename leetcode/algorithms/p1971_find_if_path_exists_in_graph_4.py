from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]],
                  source: int, destination: int) -> bool:
        roots = list(range(n))

        for x, y in edges:
            self._union(roots, x, y)

        return self._find_root(roots, source) \
            == self._find_root(roots, destination)

    def _find_root(self, roots, x):
        while roots[x] != x:
            x = roots[roots[x]]

        return x

    def _union(self, roots, x, y):
        root_x = self._find_root(roots, x)
        root_y = self._find_root(roots, y)

        if root_x != root_y:
            roots[root_x] = root_y
