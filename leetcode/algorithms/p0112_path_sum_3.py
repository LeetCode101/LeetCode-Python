from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            node, sum_so_far = queue.popleft()

            if not node.left and not node.right and sum_so_far == targetSum:
                return True

            if node.left:
                queue.append((node.left, sum_so_far + node.left.val))

            if node.right:
                queue.append((node.right, sum_so_far + node.right.val))
