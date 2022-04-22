import unittest
from leetcode.algorithms.p0064_minimum_path_sum_1 import Solution


class TestMinimumPathSum(unittest.TestCase):
    def test_minimum_path_sum(self):
        solution = Solution()

        self.assertEqual(7, solution.minPathSum(
            [[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
        self.assertEqual(12, solution.minPathSum([[1, 2, 3], [4, 5, 6]]))
