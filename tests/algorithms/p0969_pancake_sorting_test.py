import unittest
from leetcode.algorithms.p0969_pancake_sorting import Solution


class TestPancakeSorting(unittest.TestCase):
    def test_pancake_sorting(self):
        solution = Solution()

        self.assertListEqual([3, 4, 2, 3, 1, 2, 1, 1], solution.pancakeSort(
            [3, 2, 4, 1]))
        self.assertListEqual([3, 3, 2, 2, 1, 1], solution.pancakeSort(
            [1, 2, 3]))
