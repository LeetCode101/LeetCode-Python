from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._dfs(root, 0)

        return root

    def _dfs(self, root, value):
        if not root:
            return value

        right = self._dfs(root.right, value)
        left = self._dfs(root.left, root.val + right)

        root.val = root.val + right

        return left
