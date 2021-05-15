class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []

        self._inorder(root, values)

        return self._convert_sorted_array_to_bst(values, 0, len(values) - 1)

    def _inorder(self, root, values):
        if not root:
            return

        self._inorder(root.left, values)
        values.append(root.val)
        self._inorder(root.right, values)

    def _convert_sorted_array_to_bst(self, values, low, high):
        if low > high:
            return None

        middle = low + (high - low) // 2
        root = TreeNode(values[middle])
        root.left = self._convert_sorted_array_to_bst(
            values, low, middle - 1)
        root.right = self._convert_sorted_array_to_bst(
            values, middle + 1, high)

        return root
