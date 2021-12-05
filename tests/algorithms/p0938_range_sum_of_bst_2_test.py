import unittest
from leetcode.algorithms.p0938_range_sum_of_bst_2 import Solution, TreeNode


class TestRangeSumOfBST(unittest.TestCase):
    def test_range_sum_of_bst(self):
        solution = Solution()
        root1 = TreeNode(
            10,
            TreeNode(5, TreeNode(3), TreeNode(7)),
            TreeNode(15, None, TreeNode(18))
        )
        root2 = TreeNode(
            18,
            TreeNode(
                9,
                TreeNode(6, TreeNode(3)),
                TreeNode(15, TreeNode(12))
            ),
            TreeNode(
                27,
                TreeNode(24, TreeNode(21)),
                TreeNode(30)
            )
        )

        self.assertEqual(32, solution.rangeSumBST(root1, 7, 15))
        self.assertEqual(63, solution.rangeSumBST(root2, 18, 24))
