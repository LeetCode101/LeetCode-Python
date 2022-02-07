from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) \
            -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]

        if root.val <= target:
            split = self.splitBST(root.right, target)
            root.right = split[0]

            return [root, split[1]]
        else:
            split = self.splitBST(root.left, target)
            root.left = split[1]

            return [split[0], root]
