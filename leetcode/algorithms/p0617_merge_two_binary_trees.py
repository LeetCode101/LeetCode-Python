from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        left = self.mergeTrees(root1.left if root1 else None,
                               root2.left if root2 else None)
        right = self.mergeTrees(root1.right if root1 else None,
                                root2.right if root2 else None)

        if root1 and root2:
            new_root = TreeNode(root1.val + root2.val, left, right)

            return new_root
        elif root1:
            root1.left = left
            root1.right = right

            return root1
        else:
            root2.left = left
            root2.right = right

            return root2
