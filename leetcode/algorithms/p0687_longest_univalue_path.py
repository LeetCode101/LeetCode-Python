from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)

        return self.longest

    def _dfs(self, root):
        if not root:
            return 0

        left_longest = self._dfs(root.left)
        right_longest = self._dfs(root.right)

        left = left_longest + 1 if root.left and root.left.val == root.val \
            else 0
        right = right_longest + 1 if root.right and root.right.val == root.val \
            else 0

        self.longest = max(self.longest, left + right)

        return max(left, right)

        
