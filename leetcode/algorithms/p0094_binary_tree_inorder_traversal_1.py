from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []

        self._traversal(root, values)

        return values

    def _traversal(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return

        self._traversal(root.left, values)

        values.append(root.val)

        self._traversal(root.right, values)
