import unittest
from leetcode.algorithms.p1202_smallest_string_with_swaps import Solution


class TestSmallestStringWithSwaps(unittest.TestCase):
    def test_smallest_string_with_swaps(self):
        solution = Solution()

        self.assertEqual('dqwyt', solution.smallestStringWithSwaps(
            'qdwyt', [[2, 3], [3, 2], [0, 1], [4, 0], [3, 2]]))
        self.assertEqual('bacd', solution.smallestStringWithSwaps(
            'dcab', [[0, 3], [1, 2]]))
        self.assertEqual('abcd', solution.smallestStringWithSwaps(
            'dcab', [[0, 3], [1, 2], [0, 2]]))
        self.assertEqual('abc', solution.smallestStringWithSwaps(
            'cba', [[0, 1], [1, 2]]))
