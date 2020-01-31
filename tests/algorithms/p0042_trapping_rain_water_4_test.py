import unittest
from leetcode.algorithms.p0042_trapping_rain_water_4 import Solution


class TestTrappingRainWater(unittest.TestCase):
    def test_trapping_rain_water(self):
        solution = Solution()

        self.assertEqual(0, solution.trap([]))
        self.assertEqual(
            6, solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
