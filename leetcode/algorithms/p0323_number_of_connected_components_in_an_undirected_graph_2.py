from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n
        roots = list(range(n))

        for a, b in edges:
            root_a = self._get_root(roots, a)
            root_b = self._get_root(roots, b)

            if root_a != root_b:
                roots[root_a] = root_b
                count -= 1

        return count

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x
