import unittest
from leetcode.algorithms.p0962_maximum_width_ramp import Solution


class TestMaximumWidthRamp(unittest.TestCase):
    def test_maximum_width_ramp(self):
        solution = Solution()

        self.assertEqual(4, solution.maxWidthRamp([6, 0, 8, 2, 1, 5]))
        self.assertEqual(7, solution.maxWidthRamp(
            [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
