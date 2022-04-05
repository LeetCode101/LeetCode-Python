import unittest
from leetcode.algorithms.p0659_split_array_into_consecutive_subsequences \
    import Solution


class TestSplitArrayIntoConsecutiveSubsequences(unittest.TestCase):
    def test_split_array_into_consecutive_subsequences(self):
        solution = Solution()

        self.assertFalse(solution.isPossible(
            [4, 5, 6, 6, 7, 8, 9, 10, 10, 11]))
        self.assertFalse(solution.isPossible([1, 2, 3, 5, 5, 6, 7]))
        self.assertTrue(solution.isPossible([1, 2, 3, 3, 4, 5]))
        self.assertTrue(solution.isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
        self.assertFalse(solution.isPossible([1, 2, 3, 4, 4, 5]))
