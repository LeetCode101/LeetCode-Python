import unittest
from leetcode.algorithms.p1776_car_fleet_ii import Solution


class TestCarFleet(unittest.TestCase):
    def test_car_fleet(self):
        solution = Solution()

        self.assertListEqual([1.00000, -1.00000, 3.00000, -1.00000],
                             solution.getCollisionTimes(
                                 [[1, 2], [2, 1], [4, 3], [7, 2]]))
        self.assertListEqual([2.00000, 1.00000, 1.50000, -1.00000],
                             solution.getCollisionTimes(
                                 [[3, 4], [5, 4], [6, 3], [9, 1]]))
