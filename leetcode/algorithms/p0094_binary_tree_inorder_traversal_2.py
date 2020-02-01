from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            top = stack.pop()
            values.append(top.val)

            if top.right:
                current = top.right

        return values
