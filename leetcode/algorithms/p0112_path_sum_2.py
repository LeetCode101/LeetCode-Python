class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, sum_so_far = stack.pop()

            if not node.left and not node.right and sum_so_far == targetSum:
                return True

            if node.left:
                stack.append((node.left, sum_so_far + node.left.val))

            if node.right:
                stack.append((node.right, sum_so_far + node.right.val))
