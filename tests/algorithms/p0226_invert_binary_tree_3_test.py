import unittest
from leetcode.algorithms.p0226_invert_binary_tree_3 import Solution, TreeNode
from tests.algorithms.binary_tree_helper import preorder


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9))
        )

        self.assertListEqual([], preorder(solution.invertTree(None)))
        self.assertListEqual([4, 7, 9, 6, 2, 3, 1], preorder(
            solution.invertTree(root)))
