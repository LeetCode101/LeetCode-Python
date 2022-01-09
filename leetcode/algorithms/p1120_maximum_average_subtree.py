from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        _, _, max_avg = self._max(root)

        return max_avg

    def _max(self, root):
        if not root:
            return 0, 0, 0

        left_sum, left_count, left_avg_max = self._max(root.left)
        right_sum, right_count, right_avg_max = self._max(root.right)
        current_sum = left_sum + right_sum + root.val
        current_count = left_count + right_count + 1
        current_avg = current_sum / current_count

        return current_sum, current_count, \
            max(left_avg_max, right_avg_max, current_avg)
