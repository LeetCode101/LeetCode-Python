class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        numbers = []
        self._inorder_traversal(root, numbers)

        for i in range(1, len(numbers)):
            if numbers[i] <= numbers[i - 1]:
                return False

        return True

    def _inorder_traversal(self, root: TreeNode, numbers):
        if not root:
            return

        self._inorder_traversal(root.left, numbers)

        numbers.append(root.val)

        self._inorder_traversal(root.right, numbers)
