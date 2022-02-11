import unittest
from leetcode.algorithms.p0135_candy import Solution


class TestCandy(unittest.TestCase):
    def test_candy(self):
        solution = Solution()

        self.assertEqual(7, solution.candy([1, 3, 2, 2, 1]))
        self.assertEqual(5, solution.candy([1, 0, 2]))
        self.assertEqual(4, solution.candy([1, 2, 2]))
