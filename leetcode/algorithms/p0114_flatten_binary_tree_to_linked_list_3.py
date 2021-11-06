from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self._dfs(root)

    def _dfs(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        left = self._dfs(root.left)
        right = self._dfs(root.right)

        if left:
            root.right = left

            while left.right:
                left = left.right

            left.right = right

        root.left = None

        return root
