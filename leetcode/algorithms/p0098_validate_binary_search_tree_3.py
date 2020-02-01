import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        current = root
        prev_value = -sys.maxsize

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if current.val <= prev_value:
                return False

            prev_value = current.val
            current = current.right

        return True
