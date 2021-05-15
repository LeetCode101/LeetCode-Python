class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        return abs(left_height - right_height) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

    def _get_height(self, root):
        if not root:
            return 0

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        return max(left_height, right_height) + 1
