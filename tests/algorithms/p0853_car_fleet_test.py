import unittest
from leetcode.algorithms.p0853_car_fleet import Solution


class TestCarFleet(unittest.TestCase):
    def test_car_fleet(self):
        solution = Solution()

        self.assertEqual(3, solution.carFleet(
            12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
        self.assertEqual(1, solution.carFleet(10, [3], [3]))
