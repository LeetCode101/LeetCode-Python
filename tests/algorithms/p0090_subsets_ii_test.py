import unittest
from leetcode.algorithms.p0090_subsets_ii import Solution


class TestSubsets(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()

        self.assertListEqual(
            sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
            solution.subsetsWithDup([1, 2, 2])
        )
