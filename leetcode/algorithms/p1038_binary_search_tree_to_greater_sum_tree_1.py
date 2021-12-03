class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sorted_values = []

        self._inorder(root, sorted_values)

        n = len(sorted_values)
        sums = [0] * n

        for i in range(n - 1, -1, -1):
            sums[i] += sorted_values[i] + (sums[i + 1] if i + 1 < n else 0)

        sums_map = {sorted_values[i]: sums[i] for i in range(n)}
        stack = [root]

        while stack:
            node = stack.pop()
            node.val = sums_map[node.val]

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root

    def _inorder(self, root, values):
        if not root:
            return

        self._inorder(root.left, values)

        values.append(root.val)

        self._inorder(root.right, values)
