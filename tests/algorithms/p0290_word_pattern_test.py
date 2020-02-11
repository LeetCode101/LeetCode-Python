import unittest
from leetcode.algorithms.p0290_word_pattern import Solution


class TestWordPattern(unittest.TestCase):
    def test_word_pattern(self):
        solution = Solution()

        self.assertFalse(solution.wordPattern('a', 'b c'))
        self.assertTrue(solution.wordPattern('abba', 'dog cat cat dog'))
        self.assertFalse(solution.wordPattern('abba', 'dog cat cat fish'))
