import unittest
from leetcode.algorithms.p0437_path_sum_iii import Solution, TreeNode


class TestPathSum(unittest.TestCase):
    def test_path_sum(self):
        solution = Solution()
        a = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
        )

        self.assertEqual(3, solution.pathSum(a, 22))
