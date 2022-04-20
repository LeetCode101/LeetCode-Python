import unittest
from leetcode.algorithms \
    .p1218_longest_arithmetic_subsequence_of_given_difference_2 import Solution


class TestLongestArithmeticSubsequenceOfGivenDifference(unittest.TestCase):
    def test_longest_arithmetic_subsequence_of_given_difference(self):
        solution = Solution()

        self.assertEqual(4, solution.longestSubsequence([1, 2, 3, 4], 1))
        self.assertEqual(4, solution.longestSubsequence(
            [1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
