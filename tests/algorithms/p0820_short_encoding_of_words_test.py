import unittest
from leetcode.algorithms.p0820_short_encoding_of_words import Solution


class TestShortEncodingOfWords(unittest.TestCase):
    def test_short_encoding_of_words(self):
        solution = Solution()

        self.assertEqual(10, solution.minimumLengthEncoding(
            ['time', 'me', 'bell']))
        self.assertEqual(2, solution.minimumLengthEncoding(['t']))
