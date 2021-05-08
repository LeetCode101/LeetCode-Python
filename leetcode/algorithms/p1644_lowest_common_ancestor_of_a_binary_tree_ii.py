class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.node_found_count = 0

    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = self._lowest_common_ancestor(root, p, q)

        return node if self.node_found_count == 2 else None

    def _lowest_common_ancestor(self, root, p, q):
        if not root:
            return root

        left = self._lowest_common_ancestor(root.left, p, q)
        right = self._lowest_common_ancestor(root.right, p, q)

        if root.val == p.val or root.val == q.val:
            self.node_found_count += 1

            return root

        if left and right:
            return root
        else:
            return left or right
