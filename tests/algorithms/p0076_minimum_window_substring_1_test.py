import unittest
from leetcode.algorithms.p0076_minimum_window_substring_1 import Solution


class TestMinimumWindowSubstring(unittest.TestCase):
    def test_minimum_window_substring(self):
        solution = Solution()

        self.assertEqual('BANC', solution.minWindow('ADOBECODEBANC', 'ABC'))
