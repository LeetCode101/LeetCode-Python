class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        return self._has_path_sum(root, targetSum)

    def _has_path_sum(self, root, target):
        if root.left is None and root.right is None:
            return root.val == target
        else:
            path_in_left = root.left and self._has_path_sum(
                root.left, target - root.val)
            path_in_right = root.right and self._has_path_sum(
                root.right, target - root.val)

            return path_in_left or path_in_right
