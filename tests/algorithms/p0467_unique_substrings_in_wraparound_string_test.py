import unittest
from leetcode.algorithms.p0467_unique_substrings_in_wraparound_string \
    import Solution


class TestUniqueSubstringsInWraparoundString(unittest.TestCase):
    def test_unique_substrings_in_wraparound_string(self):
        solution = Solution()

        self.assertEqual(1, solution.findSubstringInWraproundString('a'))
        self.assertEqual(2, solution.findSubstringInWraproundString('cac'))
        self.assertEqual(6, solution.findSubstringInWraproundString('zab'))
