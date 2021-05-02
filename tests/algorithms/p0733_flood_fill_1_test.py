import unittest
from leetcode.algorithms.p0733_flood_fill_1 import Solution


class TestFloodFill(unittest.TestCase):
    def test_flood_fill(self):
        solution = Solution()

        self.assertListEqual([], solution.floodFill([], 1, 1, 1))
        self.assertListEqual([[2, 2, 2], [2, 2, 0], [2, 0, 1]],
                             solution.floodFill([[1, 1, 1], [1, 1, 0],
                                                 [1, 0, 1]], 1, 1, 2))
