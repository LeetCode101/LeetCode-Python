import unittest
from leetcode.algorithms.p0712_minimum_ascii_delete_sum_for_two_strings \
    import Solution


class TestMinimumASCIIDeleteSumForTwoStrings(unittest.TestCase):
    def test_minimum_ascii_delete_sum_for_two_strings(self):
        solution = Solution()

        self.assertEqual(231, solution.minimumDeleteSum('sea', 'eat'))
        self.assertEqual(403, solution.minimumDeleteSum('delete', 'leet'))
