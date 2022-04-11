import unittest
from leetcode.algorithms.p0078_subsets import Solution


class TestSubsets(unittest.TestCase):
    def test_subsets(self):
        solution = Solution()

        self.assertListEqual(
            sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
            solution.subsets([1, 2, 3])
        )
