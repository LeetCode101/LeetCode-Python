class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self._dfs(root, root.val, 0)

    def _dfs(self, root, prev_value, length_so_far):
        if not root:
            return length_so_far

        length_so_far = length_so_far + 1 if prev_value + 1 == root.val else 1

        left_length = self._dfs(root.left, root.val, length_so_far)
        right_length = self._dfs(root.right, root.val, length_so_far)

        return max(max(left_length, right_length), length_so_far)
