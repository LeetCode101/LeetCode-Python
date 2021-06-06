import unittest
from leetcode.algorithms.p0077_combinations_1 import Solution


class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        solution = Solution()

        self.assertListEqual(sorted([
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]), sorted(solution.combine(4, 2)))
