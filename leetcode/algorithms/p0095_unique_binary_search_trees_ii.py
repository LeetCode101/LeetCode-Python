from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self._generate_trees(1, n)

    def _generate_trees(self, low, high):
        if low > high:
            return [None]

        nodes = []

        for i in range(low, high + 1):
            left_nodes = self._generate_trees(low, i - 1)
            right_nodes = self._generate_trees(i + 1, high)

            for left in left_nodes:
                for right in right_nodes:
                    nodes.append(TreeNode(i, left, right))

        return nodes
