import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self._is_valid(root.left, -sys.maxsize, root.val) and \
            self._is_valid(root.right, root.val, sys.maxsize)

    def _is_valid(self, root: TreeNode, low: int, high: int) -> bool:
        if not root:
            return True

        if root.val <= low or root.val >= high:
            return False

        return self._is_valid(root.left, low, root.val) and \
            self._is_valid(root.right, root.val, high)
