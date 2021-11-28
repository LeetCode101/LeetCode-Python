import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        largest = 0

        while stack:
            node = stack.pop()
            is_bst, size = self._is_bst(node)

            if is_bst:
                largest = max(largest, size)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return largest

    def _is_bst(self, root):
        stack = []
        current = root
        prev_value = -sys.maxsize
        size = 0

        while current or stack:
            while current:
                size += 1
                stack.append(current)
                current = current.left

            current = stack.pop()

            if current.val <= prev_value:
                return False, 0

            prev_value = current.val
            current = current.right

        return True, size
