class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0

        return max(left, right) + 1
