import unittest
from leetcode.algorithms.p0110_balanced_binary_tree_2 import Solution, TreeNode


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
        root3 = TreeNode(
            1,
            TreeNode(
                1,
                TreeNode(
                    2,
                    TreeNode(
                        3,
                        TreeNode(4),
                        TreeNode(4)
                    ),
                    TreeNode(3)
                )
            ),
            TreeNode(2)
        )
        root4 = TreeNode(
            1,
            TreeNode(2),
            TreeNode(
                1,
                TreeNode(
                    2,
                    TreeNode(
                        3,
                        TreeNode(4),
                        TreeNode(4)
                    ),
                    TreeNode(3)
                )
            )
        )

        self.assertTrue(solution.isBalanced(None))
        self.assertTrue(solution.isBalanced(root1))
        self.assertFalse(solution.isBalanced(root2))
        self.assertFalse(solution.isBalanced(root3))
        self.assertFalse(solution.isBalanced(root4))
