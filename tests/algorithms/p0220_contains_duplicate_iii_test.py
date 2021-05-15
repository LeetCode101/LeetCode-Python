import unittest
from leetcode.algorithms.p0220_contains_duplicate_iii import Solution


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = Solution()

        self.assertTrue(solution.containsNearbyAlmostDuplicate(
            [1, 0, 1, 1], 1, 2))
        self.assertFalse(solution.containsNearbyAlmostDuplicate(
            [1, 5, 9, 1, 5, 9], 2, 3))
