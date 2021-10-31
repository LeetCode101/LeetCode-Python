import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        parents, queue, visited = {}, collections.deque([(target, 0)]), set()

        self._get_parents(root, None, parents)

        while queue:
            node, distance = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            if distance == k:
                result.append(node.val)

            if node.left:
                queue.append((node.left, distance + 1))

            if node.right:
                queue.append((node.right, distance + 1))

            if node in parents and parents[node]:
                queue.append((parents[node], distance + 1))

        return result

    def _get_parents(self, root, parent, parents):
        parents[root] = parent

        if root.left:
            self._get_parents(root.left, root, parents)

        if root.right:
            self._get_parents(root.right, root, parents)
