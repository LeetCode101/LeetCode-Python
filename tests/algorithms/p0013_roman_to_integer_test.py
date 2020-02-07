import unittest
from leetcode.algorithms.p0013_roman_to_integer import Solution


class TestRomanToInteger(unittest.TestCase):
    def test_roman_to_integer(self):
        solution = Solution()

        self.assertEqual(3, solution.romanToInt('III'))
        self.assertEqual(4, solution.romanToInt('IV'))
        self.assertEqual(9, solution.romanToInt('IX'))
        self.assertEqual(58, solution.romanToInt('LVIII'))
        self.assertEqual(1994, solution.romanToInt('MCMXCIV'))
