from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        roots = list(range(n))

        for a, b in edges:
            root_a = self._get_root(roots, a)
            root_b = self._get_root(roots, b)

            if root_a == root_b:
                return False

            roots[root_a] = root_b

        return len(edges) == n - 1

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x
