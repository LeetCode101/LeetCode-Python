import unittest
from leetcode.algorithms.p0938_range_sum_of_bst_1 import Solution, TreeNode


class TestRangeSumOfBST(unittest.TestCase):
    def test_range_sum_of_bst(self):
        solution = Solution()
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(3), TreeNode(7)),
            TreeNode(15, None, TreeNode(18))
        )

        self.assertEqual(32, solution.rangeSumBST(root, 7, 15))
