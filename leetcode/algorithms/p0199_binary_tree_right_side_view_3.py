from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        order = []

        self._dfs(root, 1, order)

        return order

    def _dfs(self, root, level, order):
        if not root:
            return

        if len(order) < level:
            order.append(root.val)

        if root.right:
            self._dfs(root.right, level + 1, order)

        if root.left:
            self._dfs(root.left, level + 1, order)
