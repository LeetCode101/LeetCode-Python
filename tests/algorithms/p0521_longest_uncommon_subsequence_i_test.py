import unittest
from leetcode.algorithms.p0521_longest_uncommon_subsequence_i import Solution


class TestLongestUncommonSubsequence(unittest.TestCase):
    def test_longest_uncommon_subsequence(self):
        solution = Solution()

        self.assertEqual(3, solution.findLUSlength('aba', 'cdc'))
        self.assertEqual(-1, solution.findLUSlength('a', 'a'))
