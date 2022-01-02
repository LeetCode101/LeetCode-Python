from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time Limit Exceeded!
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: List[TreeNode]) \
            -> 'TreeNode':
        return self._divide_and_conquer(root, nodes, 0, len(nodes) - 1)

    def _divide_and_conquer(self, root, nodes, start, end):
        if start > end:
            return None
        elif start == end:
            return nodes[start]
        else:
            middle = start + (end - start) // 2
            p = self._divide_and_conquer(root, nodes, start, middle)
            q = self._divide_and_conquer(root, nodes, middle + 1, end)

            return self._lowest_common_ancestor(root, p, q)

    def _lowest_common_ancestor(self, root: TreeNode,
                                p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or p.val == root.val or q.val == root.val:
            return root

        left = self._lowest_common_ancestor(root.left, p, q)
        right = self._lowest_common_ancestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
