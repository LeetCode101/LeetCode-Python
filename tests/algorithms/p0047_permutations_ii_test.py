import unittest
from leetcode.algorithms.p0047_permutations_ii import Solution


class TestPermutations(unittest.TestCase):
    def test_permutations(self):
        solution = Solution()

        self.assertListEqual([[1, 1, 2], [1, 2, 1], [2, 1, 1]],
                             solution.permuteUnique([1, 1, 2]))
