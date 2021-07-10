class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self._dfs(root)[0]

    def _dfs(self, root):
        if not root:
            return 0, 0

        left_diameter, left_depth = self._dfs(root.left)
        right_diameter, right_depth = self._dfs(root.right)
        diameter = max(left_diameter, right_diameter, left_depth + right_depth)
        depth = 1 + max(left_depth, right_depth)

        return diameter, depth
