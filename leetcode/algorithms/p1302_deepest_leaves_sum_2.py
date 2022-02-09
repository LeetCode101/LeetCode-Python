from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level_sum = []

        self._dfs(root, 0, level_sum)

        return level_sum[-1]

    def _dfs(self, root, level, level_sum):
        if level == len(level_sum):
            level_sum.append(0)

        level_sum[level] += root.val

        if root.left:
            self._dfs(root.left, level + 1, level_sum)

        if root.right:
            self._dfs(root.right, level + 1, level_sum)
