import unittest
from leetcode.algorithms.p0333_largest_bst_subtree_2 import Solution, TreeNode


class TestLargestBSTSubtree(unittest.TestCase):
    def test_largest_bst_subtree(self):
        solution = Solution()
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(1), TreeNode(8)),
            TreeNode(15, None, TreeNode(7))
        )

        self.assertEqual(3, solution.largestBSTSubtree(root))
        self.assertEqual(0, solution.largestBSTSubtree(None))
