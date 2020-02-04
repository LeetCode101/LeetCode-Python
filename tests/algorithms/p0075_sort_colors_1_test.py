import unittest
from leetcode.algorithms.p0075_sort_colors_1 import Solution


class TestSortColors(unittest.TestCase):
    def test_sort_colors(self):
        solution = Solution()
        colors = [2, 0, 2, 1, 1, 0]
        solution.sortColors(colors)

        self.assertListEqual([0, 0, 1, 1, 2, 2], colors)
