import unittest
from leetcode.algorithms.p0014_longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        solution = Solution()

        self.assertEqual('', solution.longestCommonPrefix([]))
        self.assertEqual('hello', solution.longestCommonPrefix(['hello']))
        self.assertEqual('fl', solution.longestCommonPrefix(
            ['flower', 'flow', 'flight']))
        self.assertEqual('', solution.longestCommonPrefix(
            ['dog', 'racecar', 'car']))
