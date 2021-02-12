import unittest
from leetcode.algorithms.p0119_pascals_triangle_ii_2 import Solution


class TestPascalsTriangle(unittest.TestCase):
    def test_pascals_triangle(self):
        solution = Solution()

        self.assertListEqual([1, 4, 6, 4, 1], solution.getRow(4))
