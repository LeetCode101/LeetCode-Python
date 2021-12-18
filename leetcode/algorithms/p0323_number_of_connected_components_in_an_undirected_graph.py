from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = list(range(n))

        for a, b in edges:
            self._union(roots, a, b)

        components = set()

        for root in roots:
            components.add(self._get_root(roots, root))

        return len(components)

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x

    def _union(self, roots, a, b):
        root_a = self._get_root(roots, a)
        root_b = self._get_root(roots, b)

        roots[root_a] = root_b
