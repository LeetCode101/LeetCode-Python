from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves, _ = self._dfs(root)

        return moves

    def _dfs(self, root):
        if not root:
            return 0, 0

        left_moves, left_balance = self._dfs(root.left)
        right_moves, right_balance = self._dfs(root.right)
        balance = root.val + left_balance + right_balance - 1
        moves = left_moves + right_moves + abs(balance)

        return moves, balance
