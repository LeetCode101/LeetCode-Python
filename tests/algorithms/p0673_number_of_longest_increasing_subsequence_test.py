import unittest
from leetcode.algorithms.p0673_number_of_longest_increasing_subsequence \
    import Solution


class TestNumberOfLongestIncreasingSubsequence(unittest.TestCase):
    def test_number_of_longest_increasing_subsequence(self):
        solution = Solution()

        self.assertEqual(3, solution.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
        self.assertEqual(2, solution.findNumberOfLIS([1, 3, 5, 4, 7]))
        self.assertEqual(5, solution.findNumberOfLIS([2, 2, 2, 2, 2]))
