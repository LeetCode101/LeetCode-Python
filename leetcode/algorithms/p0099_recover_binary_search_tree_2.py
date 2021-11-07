from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while self._dfs(root, None, None):
            pass

    def _dfs(self, root, min_node, max_node):
        if not root:
            return False

        if min_node and root.val < min_node.val:
            root.val, min_node.val = min_node.val, root.val

            return True

        if max_node and root.val > max_node.val:
            root.val, max_node.val = max_node.val, root.val

            return True

        return self._dfs(root.left, min_node, root) \
            or self._dfs(root.right, root, max_node)
