import unittest
from leetcode.algorithms\
    .p1671_minimum_number_of_removals_to_make_mountain_array import Solution


class TestMinimumNumberOfRemovalsToMakeMountainArray(unittest.TestCase):
    def test_minimum_number_of_removals_to_make_mountain_array(self):
        solution = Solution()

        self.assertEqual(0, solution.minimumMountainRemovals([1, 3, 1]))
        self.assertEqual(3, solution.minimumMountainRemovals(
            [2, 1, 1, 5, 6, 2, 3, 1]))
        self.assertEqual(4, solution.minimumMountainRemovals(
            [4, 3, 2, 1, 1, 2, 3, 1]))
        self.assertEqual(1, solution.minimumMountainRemovals(
            [1, 2, 3, 4, 4, 3, 2, 1]))
