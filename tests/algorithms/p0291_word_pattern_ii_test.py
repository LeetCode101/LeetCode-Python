import unittest
from leetcode.algorithms.p0291_word_pattern_ii import Solution


class TestWordPattern(unittest.TestCase):
    def test_word_pattern(self):
        solution = Solution()

        self.assertFalse(solution.wordPatternMatch('ab', 'aa'))
        self.assertTrue(solution.wordPatternMatch('abab', 'redblueredblue'))
        self.assertTrue(solution.wordPatternMatch('aaaa', 'asdasdasdasd'))
        self.assertFalse(solution.wordPatternMatch('aabb', 'xyzabcxzyabc'))
