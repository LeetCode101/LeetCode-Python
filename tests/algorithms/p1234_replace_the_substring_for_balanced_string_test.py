import unittest
from leetcode.algorithms.p1234_replace_the_substring_for_balanced_string \
    import Solution


class TestReplaceTheSubstringForBalancedString(unittest.TestCase):
    def test_replace_the_substring_for_balanced_string(self):
        solution = Solution()

        self.assertEqual(0, solution.balancedString('QWER'))
        self.assertEqual(2, solution.balancedString('QQQW'))
