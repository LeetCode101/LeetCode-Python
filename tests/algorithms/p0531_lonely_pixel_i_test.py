import unittest
from leetcode.algorithms.p0531_lonely_pixel_i import Solution


class TestLonelyPixel(unittest.TestCase):
    def test_lonely_pixel(self):
        solution = Solution()

        self.assertEqual(3, solution.findLonelyPixel(
            [['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']]))
        self.assertEqual(0, solution.findLonelyPixel(
            [['B', 'B', 'B'], ['B', 'B', 'W'], ['B', 'B', 'B']]))
