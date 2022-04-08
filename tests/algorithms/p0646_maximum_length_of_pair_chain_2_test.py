import unittest
from leetcode.algorithms.p0646_maximum_length_of_pair_chain_2 import Solution


class TestMaximumLengthOfPairChain(unittest.TestCase):
    def test_maximum_length_of_pair_chain(self):
        solution = Solution()

        self.assertEqual(2, solution.findLongestChain(
            [[1, 2], [2, 3], [3, 4]]))
        self.assertEqual(3, solution.findLongestChain(
            [[1, 2], [7, 8], [4, 5]]))
