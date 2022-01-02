import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = sys.maxsize
        stack = []
        current = root
        prev = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()

            if prev:
                min_diff = min(min_diff, abs(node.val - prev.val))

            prev = node

            if node.right:
                current = node.right

        return min_diff
