import unittest
from leetcode.algorithms.p0617_merge_two_binary_trees import Solution, TreeNode
from tests.algorithms.binary_tree_helper import inorder


class TestMergeTwoBinaryTrees(unittest.TestCase):
    def test_merge_two_binary_trees(self):
        solution = Solution()
        root1 = TreeNode(
            1,
            TreeNode(3, TreeNode(5)),
            TreeNode(2)
        )
        root2 = TreeNode(
            2,
            TreeNode(1, None, TreeNode(4)),
            TreeNode(3, None, TreeNode(7))
        )

        self.assertListEqual([5, 4, 4, 3, 5, 7], inorder(
            solution.mergeTrees(root1, root2)))
