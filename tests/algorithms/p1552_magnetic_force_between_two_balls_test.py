import unittest
from leetcode.algorithms.p1552_magnetic_force_between_two_balls import Solution


class TestMagneticForceBetweenTwoBalls(unittest.TestCase):
    def test_magnetic_force_between_two_balls(self):
        solution = Solution()

        self.assertEqual(3, solution.maxDistance([1, 2, 3, 4, 7], 3))
        self.assertEqual(999999999, solution.maxDistance(
            [5, 4, 3, 2, 1, 1000000000], 2))
