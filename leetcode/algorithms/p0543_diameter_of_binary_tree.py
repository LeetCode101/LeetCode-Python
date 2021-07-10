class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        diameter = self._get_depth(root.left) + self._get_depth(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(diameter, left_diameter, right_diameter)

    def _get_depth(self, root):
        if not root:
            return 0

        return 1 + max(self._get_depth(root.left),
                       self._get_depth(root.right))
