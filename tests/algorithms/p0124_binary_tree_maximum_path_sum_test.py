import unittest
from leetcode.algorithms.p0124_binary_tree_maximum_path_sum \
    import Solution, TreeNode


class TestBinaryTreeMaximumPathSum(unittest.TestCase):
    def test_binary_tree_maximum_path_sum(self):
        solution = Solution()
        a = TreeNode(
            -10,
            TreeNode(9),
            TreeNode(20, TreeNode(15), TreeNode(7))
        )

        self.assertEqual(0, solution.maxPathSum(None))
        self.assertEqual(42, solution.maxPathSum(a))
