class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return max(self._dfs(root))

    def _dfs(self, root):
        if not root:
            return 0, 0, 0

        max_increasing_length = 1
        max_decreasing_length = 1

        left_increasing_length, left_decreasing_length, left_full_length = \
            self._dfs(root.left)
        right_increasing_length, right_decreasing_length, right_full_length = \
            self._dfs(root.right)

        if root.left:
            if root.left.val - root.val == 1:
                max_increasing_length = left_increasing_length + 1

            if root.left.val - root.val == -1:
                max_decreasing_length = left_decreasing_length + 1

        if root.right:
            if root.right.val - root.val == 1:
                max_increasing_length = max(max_increasing_length,
                                            right_increasing_length + 1)

            if root.right.val - root.val == -1:
                max_decreasing_length = max(max_decreasing_length,
                                            right_decreasing_length + 1)

        return max_increasing_length, max_decreasing_length, max(
            max_increasing_length + max_decreasing_length - 1,
            left_full_length, right_full_length)
