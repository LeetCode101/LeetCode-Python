import unittest
from leetcode.algorithms.p0041_first_missing_positive import Solution


class TestFirstMissingPositive(unittest.TestCase):
    def test_first_missing_positive(self):
        solution = Solution()

        self.assertEqual(3, solution.firstMissingPositive([1, 2, 0]))
        self.assertEqual(2, solution.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, solution.firstMissingPositive([7, 8, 9, 11, 12]))
        self.assertEqual(3, solution.firstMissingPositive([1, 2]))
