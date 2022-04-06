import unittest
from leetcode.algorithms.p1818_minimum_absolute_sum_difference import Solution


class TestMinimumAbsoluteSumDifference(unittest.TestCase):
    def test_minimum_absolute_sum_difference(self):
        solution = Solution()

        self.assertEqual(3, solution.minAbsoluteSumDiff([1, 7, 5], [2, 3, 5]))
        self.assertEqual(0, solution.minAbsoluteSumDiff(
            [2, 4, 6, 8, 10], [2, 4, 6, 8, 10]))
        self.assertEqual(20, solution.minAbsoluteSumDiff(
            [1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4]))
