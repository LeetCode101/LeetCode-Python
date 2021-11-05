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
        nodes = []

        self._preorder(root, nodes)

        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].left = None
            nodes[i - 1].right = nodes[i]
            nodes[i - 1].left = None

    def _preorder(self, root, nodes):
        if not root:
            return

        nodes.append(root)

        self._preorder(root.left, nodes)
        self._preorder(root.right, nodes)
