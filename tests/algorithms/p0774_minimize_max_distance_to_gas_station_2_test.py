import unittest
from leetcode.algorithms.p0774_minimize_max_distance_to_gas_station_2 \
    import Solution


class TestMinimizeMaxDistanceToGasStation(unittest.TestCase):
    def test_minimize_max_distance_to_gas_station(self):
        solution = Solution()

        self.assertTrue(abs(0.5 - solution.minmaxGasDist(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)) < 0.01)
        self.assertTrue(abs(14 - solution.minmaxGasDist(
            [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1)) < 0.01)
