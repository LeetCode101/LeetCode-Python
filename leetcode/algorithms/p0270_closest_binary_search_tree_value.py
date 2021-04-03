import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = sys.maxsize

        if not root:
            return closest

        node = root

        while node:
            if abs(closest - target) > abs(node.val - target):
                closest = node.val

            node = node.left if target < node.val else node.right

        return closest
