import unittest
from leetcode.algorithms.p0787_cheapest_flights_within_k_stops import Solution


class TestCheapestFlightsWithinKStops(unittest.TestCase):
    def test_cheapest_flights_within_k_stops(self):
        solution = Solution()

        self.assertEqual(200, solution.findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
        self.assertEqual(500, solution.findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
