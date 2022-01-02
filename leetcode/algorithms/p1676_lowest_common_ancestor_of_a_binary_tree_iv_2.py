from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: List[TreeNode]) \
            -> 'TreeNode':
        return self._lowest_common_ancestor(root, set(nodes))

    def _lowest_common_ancestor(self, root, nodes) -> TreeNode:
        if not root or root in nodes:
            return root

        left = self._lowest_common_ancestor(root.left, nodes)
        right = self._lowest_common_ancestor(root.right, nodes)

        if left and right:
            return root
        else:
            return left or right
