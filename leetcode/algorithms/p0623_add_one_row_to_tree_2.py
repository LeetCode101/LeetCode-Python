from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) \
            -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        self._dfs(root, val, depth, 1)

        return root

    def _dfs(self, root, value, depth, current_depth):
        if not root:
            return

        if current_depth < depth - 1:
            self._dfs(root.left, value, depth, current_depth + 1)
            self._dfs(root.right, value, depth, current_depth + 1)
        else:
            root.left = TreeNode(value, root.left)
            root.right = TreeNode(value, None, root.right)
