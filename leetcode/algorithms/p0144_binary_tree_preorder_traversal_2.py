from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        values = []
        stack = [root]

        while stack:
            current = stack.pop()
            values.append(current.val)

            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

        return values
