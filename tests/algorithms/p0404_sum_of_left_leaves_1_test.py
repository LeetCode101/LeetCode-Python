import unittest
from leetcode.algorithms.p0404_sum_of_left_leaves_1 import Solution, TreeNode


class TestSumOfLeftLeaves(unittest.TestCase):
    def test_sum_of_left_leaves(self):
        solution = Solution()
        root = TreeNode(
            3,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )

        self.assertEqual(24, solution.sumOfLeftLeaves(root))
        self.assertEqual(0, solution.sumOfLeftLeaves(TreeNode(1)))
