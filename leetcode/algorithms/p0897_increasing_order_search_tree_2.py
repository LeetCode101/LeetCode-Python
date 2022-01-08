class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self._increasing(root, None)

    def _increasing(self, root, tail):
        if not root:
            return tail

        left = self._increasing(root.left, root)
        root.left = None
        root.right = self._increasing(root.right, tail)

        return left
