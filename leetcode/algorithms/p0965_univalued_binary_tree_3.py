from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        value = root.val

        while stack:
            node = stack.pop()

            if node.val != value:
                return False

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return True
