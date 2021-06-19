import unittest
from leetcode.algorithms.p0085_maximal_rectangle import Solution


class TestMaximalRectangle(unittest.TestCase):
    def test_maximal_rectangle(self):
        solution = Solution()

        self.assertEqual(0, solution.maximalRectangle([]))
        self.assertEqual(6, solution.maximalRectangle(
            [['1', '0', '1', '0', '0'],
             ['1', '0', '1', '1', '1'],
             ['1', '1', '1', '1', '1'],
             ['1', '0', '0', '1', '0']]))
