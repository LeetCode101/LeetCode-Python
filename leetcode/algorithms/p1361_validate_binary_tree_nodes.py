import collections
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
                                rightChild: List[int]) -> bool:
        roots = list(range(n))
        parents = [[] for _ in range(n)]

        for i, child in enumerate(leftChild):
            if child != -1:
                self._union(roots, i, child)
                parents[child].append(i)

        for i, child in enumerate(rightChild):
            if child != -1:
                self._union(roots, i, child)
                parents[child].append(i)

        components = collections.defaultdict(list)

        for i in range(n):
            components[self._get_root(roots, i)].append(i)

        for root in list(components.keys()):
            if not self._is_tree_valid(n, components[root], parents):
                components.pop(root)

        return len(components) == 1

    def _get_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return x

    def _union(self, roots, a, b):
        root_a = self._get_root(roots, a)
        root_b = self._get_root(roots, b)

        roots[root_a] = root_b

    def _is_tree_valid(self, n, nodes, parents):
        if n != len(nodes):
            return False

        has_root = False

        for i in nodes:
            if not parents[i]:
                has_root = True
            elif len(parents[i]) > 1:
                return False

        return has_root
