from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        prev = None
        current = root
        stack = []
        values = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            top = stack[-1]

            if top.right and prev != top.right:
                current = top.right
            else:
                current = stack.pop()
                values.append(current.val)
                prev = current
                current = None

        return values
