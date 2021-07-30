import unittest
from leetcode.algorithms.p0472_concatenated_words_1 import Solution


class TestConcatenatedWords(unittest.TestCase):
    def test_concatenated_words(self):
        solution = Solution()

        self.assertListEqual(
            ['catsdogcats', 'dogcatsdog', 'ratcatdogcat'],
            solution.findAllConcatenatedWordsInADict(
                ['cat', 'cats', 'catsdogcats', 'dog', 'dogcatsdog',
                 'hippopotamuses', 'rat', 'ratcatdogcat']))
