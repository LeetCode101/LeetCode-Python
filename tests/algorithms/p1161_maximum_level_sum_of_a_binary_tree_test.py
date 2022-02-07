import unittest
from leetcode.algorithms.p1161_maximum_level_sum_of_a_binary_tree \
    import Solution, TreeNode


class TestMaximumLevelSumOfABinaryTree(unittest.TestCase):
    def test_maximum_level_sum_of_a_binary_tree(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(7, TreeNode(7), TreeNode(-8)),
            TreeNode(0)
        )

        self.assertEqual(2, solution.maxLevelSum(root))
