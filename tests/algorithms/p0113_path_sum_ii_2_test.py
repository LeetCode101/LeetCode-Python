import unittest
from leetcode.algorithms.p0113_path_sum_ii_2 import Solution, TreeNode


class TestPathSum(unittest.TestCase):
    def test_path_sum(self):
        solution = Solution()
        a = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
        )

        self.assertListEqual([], solution.pathSum(None, 1))
        self.assertListEqual(sorted([[5, 4, 11, 2], [5, 8, 4, 5]]),
                             sorted(solution.pathSum(a, 22)))
