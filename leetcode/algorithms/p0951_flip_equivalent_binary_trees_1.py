from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) \
            -> bool:
        if not root1 and not root2:
            return True

        if not self._equal(root1, root2):
            return False

        if self._equal(root1.left, root2.left) \
                and self._equal(root1.right, root2.right):
            return self.flipEquiv(root1.left, root2.left) \
                   and self.flipEquiv(root1.right, root2.right)
        elif self._equal(root1.left, root2.right) \
                and self._equal(root1.right, root2.left):
            return self.flipEquiv(root1.left, root2.right) \
                   and self.flipEquiv(root1.right, root2.left)
        else:
            return False

    def _equal(self, root1, root2):
        if root1 and root2:
            return root1.val == root2.val
        else:
            return not root1 and not root2
