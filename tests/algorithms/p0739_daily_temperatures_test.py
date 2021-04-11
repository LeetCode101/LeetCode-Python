import unittest
from leetcode.algorithms.p0739_daily_temperatures import Solution


class TestDailyTemperatures(unittest.TestCase):
    def test_daily_temperatures(self):
        solution = Solution()

        self.assertListEqual([1, 1, 4, 2, 1, 1, 0, 0],
                             solution.dailyTemperatures(
                                 [73, 74, 75, 71, 69, 72, 76, 73]))
