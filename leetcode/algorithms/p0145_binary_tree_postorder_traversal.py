from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self._postorder_traversal(root, values)

        return values

    def _postorder_traversal(self, root: TreeNode, values: List[int]) -> None:
        if not root:
            return

        self._postorder_traversal(root.left, values)
        self._postorder_traversal(root.right, values)

        values.append(root.val)
