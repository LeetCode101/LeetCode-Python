import unittest
from leetcode.algorithms.p1184_distance_between_bus_stops import Solution


class TestDistanceBetweenBusStops(unittest.TestCase):
    def test_distance_between_bus_stops(self):
        solution = Solution()

        self.assertEqual(1, solution.distanceBetweenBusStops(
            [1, 2, 3, 4], 0, 1))
        self.assertEqual(4, solution.distanceBetweenBusStops(
            [1, 2, 3, 4], 0, 3))
