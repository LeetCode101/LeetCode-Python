import collections
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        roots = list(range(n))
        mapping = collections.defaultdict(list)

        for a, b in pairs:
            self._union(roots, a, b)

        for i in range(n):
            root = self._get_root(roots, i)
            mapping[root].append(s[i])

        for root in mapping.keys():
            mapping[root].sort(reverse=True)

        result = []

        for i in range(n):
            root = self._get_root(roots, i)
            result.append(mapping[root].pop())

        return ''.join(result)

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x

    def _union(self, roots, a, b):
        root_a = self._get_root(roots, a)
        root_b = self._get_root(roots, b)

        roots[root_a] = root_b
