class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        current = root
        prev_sum = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.right

            current = stack.pop()
            current_value = current.val
            current.val += prev_sum
            prev_sum += current_value
            current = current.left

        return root
