class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = []
        current = root
        new_root = None
        prev = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()

            if not new_root:
                new_root = node

            if prev:
                prev.right = node

            prev = node
            prev.left = None

            if node.right:
                current = node.right

        return new_root
