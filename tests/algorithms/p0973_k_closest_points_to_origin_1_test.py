import unittest
from leetcode.algorithms.p0973_k_closest_points_to_origin_1 import Solution


class TestKClosestPointsToOrigin(unittest.TestCase):
    def test_k_closest_points_to_origin(self):
        solution = Solution()

        self.assertListEqual([], solution.kClosest([], 1))
        self.assertListEqual(
            [[-2, 2]], sorted(solution.kClosest([[1, 3], [-2, 2]], 1)))
        self.assertListEqual(
            sorted([[3, 3], [-2, 4]]),
            sorted(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2)))
