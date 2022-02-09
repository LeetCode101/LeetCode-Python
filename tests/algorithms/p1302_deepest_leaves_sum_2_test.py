import unittest
from leetcode.algorithms.p1302_deepest_leaves_sum_2 import Solution, TreeNode


class TestDeepestLeavesSum(unittest.TestCase):
    def test_deepest_leaves_sum(self):
        solution = Solution()
        root = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(4, TreeNode(7)),
                TreeNode(5)
            ),
            TreeNode(
                3,
                None,
                TreeNode(6, None, TreeNode(8))
            )
        )

        self.assertEqual(0, solution.deepestLeavesSum(None))
        self.assertEqual(15, solution.deepestLeavesSum(root))
