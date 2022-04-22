import unittest
from leetcode.algorithms.p0413_arithmetic_slices_3 import Solution


class TestArithmeticSlices(unittest.TestCase):
    def test_arithmetic_slices(self):
        solution = Solution()

        self.assertEqual(3, solution.numberOfArithmeticSlices([1, 2, 3, 4]))
        self.assertEqual(1, solution.numberOfArithmeticSlices([1, 2, 3, 5]))
