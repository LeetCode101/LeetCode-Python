from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        roots = list(range(n))
        sorted_logs = sorted(logs, key=lambda x: x[0])

        for time, x, y in sorted_logs:
            self._union(roots, x, y)

            count = 0

            for i, root in enumerate(roots):
                if i == root:
                    count += 1

            if count == 1:
                return time

        return -1

    def _get_parent(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x

    def _union(self, roots, x, y):
        root_x = self._get_parent(roots, x)
        root_y = self._get_parent(roots, y)

        if root_x != root_y:
            roots[root_x] = root_y
