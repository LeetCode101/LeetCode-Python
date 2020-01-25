class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root

        while True:
            while current:
                stack.append(current)

                current = current.left

            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val

            current = current.right
