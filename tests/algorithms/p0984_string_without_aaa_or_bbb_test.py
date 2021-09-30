import unittest
from leetcode.algorithms.p0984_string_without_aaa_or_bbb import Solution


class TestStringWithoutAAAOrBBB(unittest.TestCase):
    def test_string_without_aaa_or_bbb(self):
        solution = Solution()

        self.assertEqual('aabaa', solution.strWithout3a3b(4, 1))
        self.assertEqual('bba', solution.strWithout3a3b(1, 2))
        self.assertEqual('abab', solution.strWithout3a3b(2, 2))
