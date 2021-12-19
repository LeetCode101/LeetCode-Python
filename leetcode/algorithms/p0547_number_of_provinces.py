from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        roots = list(range(n))
        count = n

        for i in range(n):
            for j in range(n):
                if i == j or isConnected[i][j] == 0:
                    continue

                root_a = self._find_root(roots, i)
                root_b = self._find_root(roots, j)

                if root_a != root_b:
                    count -= 1
                    roots[root_a] = root_b

        return count

    def _find_root(self, roots, x):
        while x != roots[x]:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x
