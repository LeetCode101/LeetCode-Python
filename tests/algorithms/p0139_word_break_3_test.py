import unittest
from leetcode.algorithms.p0139_word_break_3 import Solution


class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        solution = Solution()

        self.assertTrue(solution.wordBreak('leetcode', ['leet', 'code']))
        self.assertTrue(solution.wordBreak('applepenapple', ['apple', 'pen']))
        self.assertFalse(solution.wordBreak(
            'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
