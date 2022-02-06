from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        stack = [(root, None)]

        while stack:
            node, parent = stack.pop()

            if parent and node is parent.left \
                    and not node.left and not node.right:
                sum += node.val

            if node.left:
                stack.append((node.left, node))

            if node.right:
                stack.append((node.right, node))

        return sum
