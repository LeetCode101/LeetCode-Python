import unittest
from leetcode.algorithms.p0273_integer_to_english_words import Solution


class TestIntegerToEnglishWords(unittest.TestCase):
    def test_integer_to_english_words(self):
        solution = Solution()
        words = 'One Billion Two Hundred Thirty Four Million Five ' \
                'Hundred Sixty Seven Thousand Eight Hundred Ninety One'

        self.assertEqual('One Hundred One', solution.numberToWords(101))
        self.assertEqual('One Thousand', solution.numberToWords(1000))
        self.assertEqual('One Thousand One', solution.numberToWords(1001))
        self.assertEqual('Ten', solution.numberToWords(10))
        self.assertEqual('One Hundred', solution.numberToWords(100))
        self.assertEqual('Twenty', solution.numberToWords(20))
        self.assertEqual(words, solution.numberToWords(1234567891))
