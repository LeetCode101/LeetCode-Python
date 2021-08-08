import unittest
from leetcode.algorithms.p0532_k_diff_pairs_in_an_array import Solution


class TestKDiffPairsInAnArray(unittest.TestCase):
    def test_k_diff_pairs_in_an_array(self):
        solution = Solution()

        self.assertEqual(1, solution.findPairs([1, 1], 0))
        self.assertEqual(2, solution.findPairs([3, 1, 4, 1, 5], 2))
        self.assertEqual(2, solution.findPairs(
            [1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3))
