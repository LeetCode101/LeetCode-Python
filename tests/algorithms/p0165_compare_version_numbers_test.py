import unittest
from leetcode.algorithms.p0165_compare_version_numbers import Solution


class TestCompareVersionNumbers(unittest.TestCase):
    def test_compare_version_numbers(self):
        solution = Solution()

        self.assertEqual(0, solution.compareVersion('1.1', '1.1.000'))
        self.assertEqual(1, solution.compareVersion('1.2', '1.1'))
        self.assertEqual(1, solution.compareVersion('1.0.1', '1'))
        self.assertEqual(-1, solution.compareVersion('7.5.2.4', '7.5.3'))
        self.assertEqual(0, solution.compareVersion('1.01', '1.001'))
