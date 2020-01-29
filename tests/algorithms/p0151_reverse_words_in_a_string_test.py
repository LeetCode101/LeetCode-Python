import unittest
from leetcode.algorithms.p0151_reverse_words_in_a_string import Solution


class TestReverseWordsInAString(unittest.TestCase):
    def test_reverse_words_in_a_string(self):
        solution = Solution()

        self.assertEqual(
            'blue is sky the', solution.reverseWords('the sky is blue'))
        self.assertEqual(
            'example good a', solution.reverseWords('a good   example'))
