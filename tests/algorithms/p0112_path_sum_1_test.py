import unittest
from leetcode.algorithms.p0112_path_sum_1 import Solution, TreeNode


class TestPathSum(unittest.TestCase):
    def test_path_sum(self):
        solution = Solution()
        a = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1)))
        )

        self.assertFalse(solution.hasPathSum(None, 0))
        self.assertTrue(solution.hasPathSum(a, 22))
