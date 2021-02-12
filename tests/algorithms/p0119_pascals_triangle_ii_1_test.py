import unittest
from leetcode.algorithms.p0119_pascals_triangle_ii_1 import Solution


class TestPascalsTriangle(unittest.TestCase):
    def test_pascals_triangle(self):
        solution = Solution()

        self.assertListEqual([1, 3, 3, 1], solution.getRow(3))
