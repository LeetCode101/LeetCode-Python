class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        return self._find_min(root, root.val)

    def _find_min(self, root: TreeNode, root_value: int) -> int:
        if root.val > root_value:
            return root.val

        if root.left:
            left_min = self._find_min(root.left, root_value)
            right_min = self._find_min(root.right, root_value)

            return self._min(left_min, right_min)

        return -1

    def _min(self, a: int, b: int) -> int:
        if a == -1:
            return b
        elif b == -1:
            return a
        else:
            return min(a, b)
