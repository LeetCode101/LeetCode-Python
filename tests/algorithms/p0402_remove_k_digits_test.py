import unittest
from leetcode.algorithms.p0402_remove_k_digits import Solution


class TestRemoveKDigits(unittest.TestCase):
    def test_remove_k_digits(self):
        solution = Solution()

        self.assertEqual('1219', solution.removeKdigits('1432219', 3))
        self.assertEqual('0', solution.removeKdigits('9', 1))
        self.assertEqual('1', solution.removeKdigits('1001', 1))
