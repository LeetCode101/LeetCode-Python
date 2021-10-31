from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        parents, stack, visited = {}, [(target, 0)], set()

        self._get_parents(root, None, parents)

        while stack:
            node, distance = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            if distance == k:
                result.append(node.val)

            if node.left:
                stack.append((node.left, distance + 1))

            if node.right:
                stack.append((node.right, distance + 1))

            if node in parents and parents[node]:
                stack.append((parents[node], distance + 1))

        return result

    def _get_parents(self, root, parent, parents):
        parents[root] = parent

        if root.left:
            self._get_parents(root.left, root, parents)

        if root.right:
            self._get_parents(root.right, root, parents)
