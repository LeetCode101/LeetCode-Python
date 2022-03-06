import unittest
from leetcode.algorithms.p2187_minimum_time_to_complete_trips import Solution


class TestMinimumTimeToCompleteTrips(unittest.TestCase):
    def test_minimum_time_to_complete_trips(self):
        solution = Solution()

        self.assertEqual(3, solution.minimumTime([1, 2, 3], 5))
        self.assertEqual(2, solution.minimumTime([2], 1))
