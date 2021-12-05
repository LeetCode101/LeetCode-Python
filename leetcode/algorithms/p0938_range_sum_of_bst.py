from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) \
            -> int:
        if not root:
            return 0

        if low <= root.val <= high:
            return self.rangeSumBST(root.left, low, root.val) \
                   + self.rangeSumBST(root.right, root.val, high) + root.val
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
