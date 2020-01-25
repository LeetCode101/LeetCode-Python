import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        second_min_value = self.find_min(root, root.val)

        return second_min_value if second_min_value != sys.maxsize else -1

    def find_min(self, root: TreeNode, root_value: int) -> int:
        if root.val > root_value:
            return root.val

        if root.left:
            left_min = self.find_min(root.left, root_value)
            right_min = self.find_min(root.right, root_value)

            return min(left_min, right_min)

        return sys.maxsize
