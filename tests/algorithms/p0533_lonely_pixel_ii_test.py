import unittest
from leetcode.algorithms.p0533_lonely_pixel_ii import Solution


class TestLonelyPixel(unittest.TestCase):
    def test_lonely_pixel(self):
        solution = Solution()

        self.assertEqual(6, solution.findBlackPixel(
            [['W', 'B', 'W', 'B', 'B', 'W'], ['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'B', 'W', 'B', 'B', 'W'],
             ['W', 'W', 'B', 'W', 'B', 'W']], 3))
        self.assertEqual(0, solution.findBlackPixel(
            [['W', 'W', 'B'], ['W', 'W', 'B'], ['W', 'W', 'B']], 1))
        self.assertEqual(9, solution.findBlackPixel(
            [['W', 'B', 'W', 'B', 'B', 'W'], ['B', 'W', 'B', 'W', 'W', 'B'],
             ['W', 'B', 'W', 'B', 'B', 'W'], ['B', 'W', 'B', 'W', 'W', 'B'],
             ['W', 'W', 'W', 'B', 'B', 'W'],
             ['B', 'W', 'B', 'W', 'W', 'B']], 3))
