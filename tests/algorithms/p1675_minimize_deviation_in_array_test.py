import unittest
from leetcode.algorithms.p1675_minimize_deviation_in_array import Solution


class TestMinimizeDeviationInArray(unittest.TestCase):
    def test_minimize_deviation_in_array(self):
        solution = Solution()

        self.assertEqual(1, solution.minimumDeviation([1, 2, 3, 4]))
        self.assertEqual(3, solution.minimumDeviation([4, 1, 5, 20, 3]))
        self.assertEqual(3, solution.minimumDeviation([2, 10, 8]))
