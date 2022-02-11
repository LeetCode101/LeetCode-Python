import unittest
from leetcode.algorithms.p0605_can_place_flowers import Solution


class TestCanPlaceFlowers(unittest.TestCase):
    def test_can_place_flowers(self):
        solution = Solution()

        self.assertTrue(solution.canPlaceFlowers([0, 0, 1, 0, 0], 1))
        self.assertTrue(solution.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
        self.assertTrue(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertFalse(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))
