import unittest
from leetcode.algorithms.p0611_valid_triangle_number import Solution


class TestValidTriangleNumber(unittest.TestCase):
    def test_valid_triangle_number(self):
        solution = Solution()

        self.assertEqual(3, solution.triangleNumber([2, 2, 3, 4]))
