from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        stack = []
        current = root

        while current or stack:
            while current:
                values.append(current.val)
                stack.append(current)
                current = current.left

            current = stack.pop()
            current = current.right

        return values
