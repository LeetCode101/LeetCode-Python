import unittest
from leetcode.algorithms.p1891_cutting_ribbons import Solution


class TestCuttingRibbons(unittest.TestCase):
    def test_cutting_ribbons(self):
        solution = Solution()

        self.assertEqual(5, solution.maxLength([9, 7, 5], 3))
        self.assertEqual(4, solution.maxLength([7, 5, 9], 4))
        self.assertEqual(0, solution.maxLength([5, 7, 9], 22))
