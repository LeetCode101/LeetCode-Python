import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        _, _, size, _ = self._dfs(root)

        return size

    def _dfs(self, root):
        if not root:
            return -sys.maxsize, sys.maxsize, 0, True

        left_min, left_max, left_size, left_valid = self._dfs(root.left)
        right_min, right_max, right_size, right_valid = self._dfs(root.right)

        if left_valid and right_valid and (left_min < root.val < right_max):
            if not root.left:
                left_max = root.val

            if not root.right:
                right_min = root.val

            return right_min, left_max, left_size + right_size + 1, True
        else:
            if left_size > right_size:
                return left_min, left_max, left_size, False
            else:
                return right_min, right_max, right_size, False
