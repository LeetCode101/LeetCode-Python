import unittest
from leetcode.algorithms.p0223_rectangle_area import Solution


class TestRectangleArea(unittest.TestCase):
    def test_rectangle_area(self):
        solution = Solution()

        self.assertEqual(45, solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
