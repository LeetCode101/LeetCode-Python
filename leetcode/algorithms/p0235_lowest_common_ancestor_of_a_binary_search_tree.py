class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) \
            -> TreeNode:
        current = root
        min_value = min(p.val, q.val)
        max_value = max(p.val, q.val)

        while current:
            if min_value > current.val:
                current = current.right
            elif max_value < current.val:
                current = current.left
            else:
                return current
