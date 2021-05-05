import unittest
from leetcode.algorithms.p0666_path_sum_iv_2 import Solution


class TestPathSum(unittest.TestCase):
    def test_path_sum(self):
        solution = Solution()

        self.assertEqual(0, solution.pathSum([]))
        self.assertEqual(12, solution.pathSum([113, 215, 221]))
        self.assertEqual(4, solution.pathSum([113, 221]))
