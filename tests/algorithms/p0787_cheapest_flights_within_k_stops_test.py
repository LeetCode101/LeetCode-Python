import unittest
from leetcode.algorithms.p0787_cheapest_flights_within_k_stops import Solution


class TestCheapestFlightsWithinKStops(unittest.TestCase):
    def test_cheapest_flights_within_k_stops(self):
        solution = Solution()

        self.assertEqual(200, solution.findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
        self.assertEqual(500, solution.findCheapestPrice(
            3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
        self.assertEqual(14, solution.findCheapestPrice(
            10, [[3, 4, 4], [2, 5, 6], [4, 7, 10], [9, 6, 5], [7, 4, 4],
                 [6, 2, 10], [6, 8, 6], [7, 9, 4], [1, 5, 4], [1, 0, 4],
                 [9, 7, 3], [7, 0, 5], [6, 5, 8], [1, 7, 6], [4, 0, 9],
                 [5, 9, 1], [8, 7, 3], [1, 2, 6], [4, 1, 5], [5, 2, 4],
                 [1, 9, 1], [7, 8, 10], [0, 4, 2], [7, 2, 8]], 6, 0, 7))
