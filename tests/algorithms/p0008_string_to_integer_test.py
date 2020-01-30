import unittest
from leetcode.algorithms.p0008_string_to_integer import Solution


class TestStringToInteger(unittest.TestCase):
    def test_string_to_integer(self):
        solution = Solution()

        self.assertEqual(42, solution.myAtoi('42'))
        self.assertEqual(-42, solution.myAtoi('   -42'))
        self.assertEqual(4193, solution.myAtoi('4193 with words'))
        self.assertEqual(0, solution.myAtoi('words and 987'))
        self.assertEqual(-2147483648, solution.myAtoi('-91283472332'))
        self.assertEqual(2147483647, solution.myAtoi('91283472332'))
        self.assertEqual(0, solution.myAtoi('    '))
