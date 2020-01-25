import unittest
from leetcode.algorithms.p0844_backspace_string_compare_2 import Solution


class TestBackspaceStringCompare(unittest.TestCase):
    def test_backspace_string_compare(self):
        solution = Solution()

        self.assertTrue(solution.backspaceCompare('a', 'a#abc##'))
        self.assertTrue(solution.backspaceCompare('ab##', 'c#d#'))
        self.assertFalse(solution.backspaceCompare('a#c', 'bc'))
        self.assertFalse(solution.backspaceCompare('a#c', 'b'))
        self.assertTrue(solution.backspaceCompare('a', 'a'))
