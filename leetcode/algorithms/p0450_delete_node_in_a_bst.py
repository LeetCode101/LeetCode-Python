class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                root.val = self._find_min(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                return root.left or root.right

        return root

    def _find_min(self, root):
        while root.left:
            root = root.left

        return root.val
