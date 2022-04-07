import unittest
from leetcode.algorithms.p1488_avoid_flood_in_the_city import Solution


class TestAvoidFloodInTheCity(unittest.TestCase):
    def test_avoid_flood_in_the_city(self):
        solution = Solution()

        self.assertListEqual([-1, -1, -1, -1], solution.avoidFlood(
            [1, 2, 3, 4]))
        self.assertListEqual([-1, -1, 2, 1, -1, -1], solution.avoidFlood(
            [1, 2, 0, 0, 2, 1]))
        self.assertListEqual([], solution.avoidFlood([1, 2, 0, 1, 2]))
