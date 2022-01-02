import unittest
from leetcode.algorithms.p0530_minimum_absolute_difference_in_bst \
    import Solution, TreeNode


class TestMinimumAbsoluteDifferenceInBST(unittest.TestCase):
    def test_minimum_absolute_difference_in_bst(self):
        solution = Solution()
        root1 = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6)
        )
        root2 = TreeNode(
            1,
            None,
            TreeNode(3, TreeNode(2))
        )

        self.assertEqual(1, solution.getMinimumDifference(root2))
        self.assertEqual(1, solution.getMinimumDifference(root1))
