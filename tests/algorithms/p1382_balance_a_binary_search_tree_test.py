import unittest
from leetcode.algorithms.p1382_balance_a_binary_search_tree \
    import Solution, TreeNode
from leetcode.algorithms.p0110_balanced_binary_tree_2 \
    import Solution as BalancedSolution


class TestBalanceABinarySearchTree(unittest.TestCase):
    def test_balance_a_binary_search_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            None,
            TreeNode(
                2,
                None,
                TreeNode(
                    3,
                    None,
                    TreeNode(4)
                )
            )
        )
        balanced = solution.balanceBST(root)

        self.assertTrue(BalancedSolution().isBalanced(balanced))
