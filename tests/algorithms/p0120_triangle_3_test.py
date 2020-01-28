import unittest
from leetcode.algorithms.p0120_triangle_3 import Solution


class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        solution = Solution()
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]

        self.assertEqual(11, solution.minimumTotal(triangle))
