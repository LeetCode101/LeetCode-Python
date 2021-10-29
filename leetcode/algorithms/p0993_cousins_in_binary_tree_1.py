from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [(root, 0, None)]
        prev_parent = None
        prev_depth = -1

        while stack:
            node, depth, parent = stack.pop()

            if node.val == x or node.val == y:
                if prev_parent:
                    return prev_parent != parent and depth == prev_depth
                else:
                    prev_parent = parent
                    prev_depth = depth

            if node.left:
                stack.append((node.left, depth + 1, node))

            if node.right:
                stack.append((node.right, depth + 1, node))

        return False
