from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) \
            -> int:
        range_sum = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                range_sum += node.val

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)
            elif node.val < low and node.right:
                stack.append(node.right)
            elif node.val > high and node.left:
                stack.append(node.left)

        return range_sum
