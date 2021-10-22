from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundary = self._get_left_boundary(root.left)
        leaves = self._get_leaves(root)
        right_boundary = self._get_right_boundary(root.right)

        return [root.val] + left_boundary + leaves + right_boundary

    def _is_leaf(self, node):
        return not node.left and not node.right

    def _get_left_boundary(self, node):
        if not node:
            return []

        order = []

        while not self._is_leaf(node):
            order.append(node.val)

            node = node.left or node.right

        return order

    def _get_right_boundary(self, node):
        if not node:
            return []

        order = []

        while not self._is_leaf(node):
            order.append(node.val)

            node = node.right or node.left

        return order[::-1]

    def _get_leaves(self, root):
        if self._is_leaf(root):
            return []

        stack = [root]
        order = []

        while stack:
            node = stack.pop()

            if self._is_leaf(node):
                order.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

        return order
