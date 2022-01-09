import unittest
from leetcode.algorithms.p1120_maximum_average_subtree \
    import Solution, TreeNode


class TestMaximumAverageSubtree(unittest.TestCase):
    def test_maximum_average_subtree(self):
        solution = Solution()
        root = TreeNode(
            5,
            TreeNode(6),
            TreeNode(1)
        )

        self.assertEqual(6, solution.maximumAverageSubtree(root))
