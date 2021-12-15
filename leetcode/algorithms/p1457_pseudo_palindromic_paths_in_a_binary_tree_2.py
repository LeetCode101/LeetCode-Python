from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, set())]
        count = 0

        while stack:
            node, prev_values = stack.pop()
            values = set.union(prev_values, {node.val}) \
                if node.val not in prev_values \
                else set.difference(prev_values, {node.val})

            if self._is_leaf(node) and len(values) <= 1:
                count += 1

            if node.left:
                stack.append((node.left, values))

            if node.right:
                stack.append((node.right, values))

        return count

    def _is_leaf(self, node):
        return not node.left and not node.right
