import unittest
from leetcode.algorithms.p0118_pascals_triangle import Solution


class TestPascalsTriangle(unittest.TestCase):
    def test_pascals_triangle(self):
        solution = Solution()
        expected_list = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]

        self.assertListEqual(expected_list, solution.generate(5))
