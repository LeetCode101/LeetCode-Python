class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self._reversed_inorder(root, 0)

        return root

    def _reversed_inorder(self, root, sum):
        if not root:
            return sum

        root.val += self._reversed_inorder(root.right, sum)

        return self._reversed_inorder(root.left, root.val)
