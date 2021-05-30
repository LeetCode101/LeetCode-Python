import unittest
from leetcode.algorithms.p0422_valid_word_square import Solution


class TestValidWordSquare(unittest.TestCase):
    def test_valid_word_square(self):
        solution = Solution()

        self.assertTrue(solution.validWordSquare([]))
        self.assertTrue(solution.validWordSquare(
            ['abcd', 'bnrt', 'crmy', 'dtye']))
        self.assertTrue(solution.validWordSquare(
            ['abcd', 'bnrt', 'crm', 'dt']))
        self.assertFalse(solution.validWordSquare(
            ['ball', 'area', 'read', 'lady']))
