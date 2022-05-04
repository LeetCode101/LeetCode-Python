import unittest
from leetcode.algorithms.p0046_permutations_1 import Solution


class TestPermutations(unittest.TestCase):
    def test_permutations(self):
        solution = Solution()

        self.assertListEqual(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            solution.permute([1, 2, 3]))
