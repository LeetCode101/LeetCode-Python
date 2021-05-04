class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or self._is_symmetric(root.left, root.right)

    def _is_symmetric(self, left, right):
        if left is None or right is None:
            return left is None and right is None

        if left.val != right.val:
            return False

        return self._is_symmetric(left.left, right.right) \
            and self._is_symmetric(left.right, right.left)
