# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self._rob(root))

    def _rob(self, root: TreeNode) -> List[int]:
        if not root:
            return [0, 0]

        left = self._rob(root.left)
        right = self._rob(root.right)
        rob = root.val + left[1] + right[1]
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return [rob, not_rob]
