import unittest
from leetcode.algorithms.p1870_minimum_speed_to_arrive_on_time import Solution


class TestMinimumSpeedToArriveOnTime(unittest.TestCase):
    def test_minimum_speed_to_arrive_on_time(self):
        solution = Solution()

        self.assertEqual(-1, solution.minSpeedOnTime([1, 1], 1.0))
        self.assertEqual(10000000, solution.minSpeedOnTime(
            [1, 1, 100000], 2.01))
        self.assertEqual(3, solution.minSpeedOnTime([1, 3, 2], 2.7))
        self.assertEqual(1, solution.minSpeedOnTime([1, 3, 2], 6))
        self.assertEqual(-1, solution.minSpeedOnTime([1, 3, 2], 1.9))
