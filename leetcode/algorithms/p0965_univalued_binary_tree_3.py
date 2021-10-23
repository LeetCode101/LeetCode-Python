from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self._dfs(root, root.val)

    def _dfs(self, root, value):
        if not root:
            return True

        if root.val != value:
            return False

        return self._dfs(root.left, value) and self._dfs(root.right, value)
