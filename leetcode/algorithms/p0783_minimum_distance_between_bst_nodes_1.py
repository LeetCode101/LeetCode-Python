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
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                min_diff = min(min_diff, node.val - self._find_max(node.left))
                stack.append(node.left)

            if node.right:
                min_diff = min(min_diff, self._find_min(node.right) - node.val)
                stack.append(node.right)

        return min_diff

    def _find_max(self, root):
        max_value = root.val

        while root:
            max_value = max(max_value, root.val)
            root = root.right

        return max_value

    def _find_min(self, root):
        min_value = root.val

        while root:
            min_value = min(min_value, root.val)
            root = root.left

        return min_value
