from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) \
            -> List[int]:
        candidate1, candidate2, parents = None, None, {}

        for a, b in edges:
            if b in parents:
                candidate1, candidate2 = [parents[b], b], [a, b]

                break

            parents[b] = a

        roots = list(range((len(edges) + 1)))

        for a, b in edges:
            if [a, b] == candidate2:
                continue

            root_a, root_b = self._get_root(roots, a), self._get_root(roots, b)

            if root_a == root_b:
                if not candidate1:
                    return [a, b]
                else:
                    return candidate1

            roots[root_a] = root_b

        return candidate2

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x
