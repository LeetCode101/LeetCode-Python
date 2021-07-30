import unittest
from leetcode.algorithms.p0472_concatenated_words_2 import Solution


class TestConcatenatedWords(unittest.TestCase):
    def test_concatenated_words(self):
        solution = Solution()

        self.assertListEqual(
            ['dogcatsdog', 'catsdogcats', 'ratcatdogcat'],
            solution.findAllConcatenatedWordsInADict(
                ['cat', 'cats', 'catsdogcats', 'dog', 'dogcatsdog',
                 'hippopotamuses', 'rat', 'ratcatdogcat']))
