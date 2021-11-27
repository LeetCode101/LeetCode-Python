from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = [(root, root.val, root.val)]
        max_diff = 0

        while stack:
            node, min_value, max_value = stack.pop()
            max_diff = max(max_diff, abs(min_value - max_value))

            if node.left:
                stack.append((node.left, min(min_value, node.left.val),
                              max(max_value, node.left.val)))

            if node.right:
                stack.append((node.right, min(min_value, node.right.val),
                              max(max_value, node.right.val)))

        return max_diff
