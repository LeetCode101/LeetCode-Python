import unittest
from leetcode.algorithms.p0110_balanced_binary_tree_1 import Solution, TreeNode


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced_binary_tree(self):
        solution = Solution()
        root1 = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )
        root2 = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(
                    3,
                    TreeNode(4),
                    TreeNode(4)
                ),
                TreeNode(3)
            ),
            TreeNode(2)
        )

        self.assertTrue(solution.isBalanced(None))
        self.assertTrue(solution.isBalanced(root1))
        self.assertFalse(solution.isBalanced(root2))
