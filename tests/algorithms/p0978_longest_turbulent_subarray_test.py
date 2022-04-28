import unittest
from leetcode.algorithms.p0978_longest_turbulent_subarray import Solution


class TestLongestTurbulentSubarray(unittest.TestCase):
    def test_longest_turbulent_subarray(self):
        solution = Solution()

        self.assertEqual(5, solution.maxTurbulenceSize(
            [9, 4, 2, 10, 7, 8, 8, 1, 9]))
        self.assertEqual(2, solution.maxTurbulenceSize([4, 8, 12, 16]))
