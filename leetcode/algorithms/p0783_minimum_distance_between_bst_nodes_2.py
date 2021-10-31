import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        min_diff = sys.maxsize
        values = []

        self._inorder(root, values)

        for i in range(1, len(values)):
            min_diff = min(min_diff, values[i] - values[i - 1])

        return min_diff

    def _inorder(self, root, values):
        if not root:
            return

        self._inorder(root.left, values)

        values.append(root.val)

        self._inorder(root.right, values)
