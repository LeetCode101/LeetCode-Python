class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = self._traverse(root)

        return nodes[k - 1].val

    def _traverse(self, root: TreeNode):
        if not root:
            return []

        return self._traverse(root.left) + [root] + self._traverse(root.right)
