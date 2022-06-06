from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        stack = []
        sum_so_far = 0

        while current or stack:
            if current:
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                sum_so_far += current.val
                current.val = sum_so_far
                current = current.left

        return root
