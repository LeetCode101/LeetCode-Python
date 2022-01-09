from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest, _ = self._dfs(root)

        return longest

    def _dfs(self, root):
        if not root:
            return 0, 0

        left_longest, left_depth = self._dfs(root.left)
        right_longest, right_depth = self._dfs(root.right)

        left = left_depth + 1 \
            if root.left and root.left.val == root.val else 0
        right = right_depth + 1 \
            if root.right and root.right.val == root.val else 0

        return max(left_longest, right_longest, left + right), max(left, right)
