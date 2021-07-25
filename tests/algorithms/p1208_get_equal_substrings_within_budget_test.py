import unittest
from leetcode.algorithms.p1208_get_equal_substrings_within_budget \
    import Solution


class TestGetEqualSubstringsWithinBudget(unittest.TestCase):
    def test_get_equal_substrings_within_budget(self):
        solution = Solution()

        self.assertEqual(3, solution.equalSubstring('abcd', 'bcdf', 3))
        self.assertEqual(1, solution.equalSubstring('abcd', 'cdef', 3))
