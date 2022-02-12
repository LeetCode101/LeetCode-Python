import unittest
from leetcode.algorithms.p0624_maximum_distance_in_arrays_2 import Solution


class TestMaximumDistanceInArrays(unittest.TestCase):
    def test_maximum_distance_in_arrays(self):
        solution = Solution()

        self.assertEqual(4, solution.maxDistance(
            [[1, 2, 3], [4, 5], [1, 2, 3]]))
        self.assertEqual(0, solution.maxDistance([[1], [1]]))
