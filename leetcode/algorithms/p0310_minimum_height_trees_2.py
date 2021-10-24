import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [n - 1]

        parent_to_children = collections.defaultdict(list)

        for edge in edges:
            parent_to_children[edge[0]].append(edge[1])
            parent_to_children[edge[1]].append(edge[0])

        queue = []

        for parent, children in parent_to_children.items():
            if len(children) == 1:
                queue.append(parent)

        while queue and len(parent_to_children) > 2:
            nodes = []

            while queue:
                node = queue.pop()
                child = parent_to_children[node][0]
                parent_to_children[child].remove(node)

                if len(parent_to_children[child]) == 1:
                    nodes.append(child)

                del parent_to_children[node]

            queue = nodes[:]

        return list(parent_to_children.keys())
