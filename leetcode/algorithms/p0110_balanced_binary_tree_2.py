class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self._get_height(root)[1]

    def _get_height(self, root):
        if not root:
            return 0, True

        left_height, balanced = self._get_height(root.left)

        if not balanced:
            return left_height, balanced

        right_height, balanced = self._get_height(root.right)

        if not balanced:
            return right_height, balanced

        height = max(left_height, right_height) + 1

        if abs(left_height - right_height) > 1:
            return height, False

        return height, True
