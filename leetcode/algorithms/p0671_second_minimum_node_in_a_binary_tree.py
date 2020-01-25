import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_value = root.val
        second_min_value = sys.maxsize
        nodes = [root]

        while nodes:
            node = nodes.pop()

            if node.val != min_value and node.val < second_min_value:
                second_min_value = node.val

            if node.left:
                nodes.append(node.left)
                nodes.append(node.right)

        return second_min_value if second_min_value != sys.maxsize else -1
