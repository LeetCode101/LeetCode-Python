import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        _, _, size = self._dfs(root)

        return size

    def _dfs(self, root):
        if not root:
            return sys.maxsize, -sys.maxsize, 0

        left_min, left_max, left_size = self._dfs(root.left)
        right_min, right_max, right_size = self._dfs(root.right)

        if left_max < root.val < right_min:
            return min(left_min, root.val), max(right_max, root.val), left_size + right_size + 1
        else:
            return -sys.maxsize, sys.maxsize, max(left_size, right_size)
