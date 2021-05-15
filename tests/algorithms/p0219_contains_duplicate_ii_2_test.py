import unittest
from leetcode.algorithms.p0219_contains_duplicate_ii_2 import Solution


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = Solution()

        self.assertTrue(solution.containsNearbyDuplicate([1, 1], 2))
        self.assertFalse(solution.containsNearbyDuplicate(
            [1, 2, 3, 1, 2, 3], 2))
