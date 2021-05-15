import unittest
from leetcode.algorithms.p0217_contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = Solution()

        self.assertTrue(solution.containsDuplicate(
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
