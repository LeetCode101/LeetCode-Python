import unittest
from leetcode.algorithms.p0727_minimum_window_subsequence import Solution


class TestMinimumWindowSubsequence(unittest.TestCase):
    def test_minimum_window_subsequence(self):
        solution = Solution()

        self.assertEqual('bcde', solution.minWindow('abcdebdde', 'bde'))
