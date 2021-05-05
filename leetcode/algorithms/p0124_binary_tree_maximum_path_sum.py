import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = -sys.maxsize

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        self._dfs(root)

        return self.max_sum

    def _dfs(self, root):
        if not root:
            return 0

        left = max(self._dfs(root.left), 0)
        right = max(self._dfs(root.right), 0)
        current_sum = root.val + left + right
        self.max_sum = max(self.max_sum, current_sum)

        return root.val + max(left, right)
