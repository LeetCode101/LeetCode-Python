from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_left = self._find_max(root, root.val, root.val)
        max_right = self._find_max(root, root.val, root.val)

        return max(max_left, max_right)

    def _find_max(self, root, min_value, max_value):
        min_value = min(root.val, min_value)
        max_value = max(root.val, max_value)

        max_left = self._find_max(root.left, min_value, max_value) \
            if root.left else abs(min_value - max_value)
        max_right = self._find_max(root.right, min_value, max_value) \
            if root.right else abs(min_value - max_value)

        return max(max_left, max_right)
