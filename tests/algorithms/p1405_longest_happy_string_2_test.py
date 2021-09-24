import unittest
from leetcode.algorithms.p1405_longest_happy_string_2 import Solution


class TestLongestHappyString(unittest.TestCase):
    def test_longest_happy_string(self):
        solution = Solution()

        self.assertEqual('ccaccbcc', solution.longestDiverseString(1, 1, 7))
        self.assertEqual('ababc', solution.longestDiverseString(2, 2, 1))
        self.assertEqual('aabaa', solution.longestDiverseString(7, 1, 0))
