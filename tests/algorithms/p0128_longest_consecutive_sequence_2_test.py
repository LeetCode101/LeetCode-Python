import unittest
from leetcode.algorithms.p0128_longest_consecutive_sequence_2 import Solution


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_longest_consecutive_sequence(self):
        solution = Solution()

        self.assertEqual(4, solution.longestConsecutive(
            [100, 4, 200, 1, 3, 2]))
        self.assertEqual(9, solution.longestConsecutive(
            [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
