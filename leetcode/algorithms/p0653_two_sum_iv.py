from typing import Set


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self._find(root, k, set())

    def _find(self, root: TreeNode, k: int, visited: Set[int]) -> bool:
        if not root:
            return False

        if k - root.val in visited:
            return True

        visited.add(root.val)

        return self._find(root.left, k, visited) or self._find(
            root.right, k, visited)
