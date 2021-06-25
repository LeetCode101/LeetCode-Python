import unittest
from leetcode.algorithms.p0522_longest_uncommon_subsequence_ii import Solution


class TestLongestUncommonSubsequence(unittest.TestCase):
    def test_longest_uncommon_subsequence(self):
        solution = Solution()

        self.assertEqual(3, solution.findLUSlength(['aba', 'cdc', 'eae']))
        self.assertEqual(-1, solution.findLUSlength(['aaa', 'aaa', 'aa']))
