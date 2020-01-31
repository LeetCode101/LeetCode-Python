import unittest
from leetcode.algorithms.p0186_reverse_words_in_a_string_ii import Solution


class TestReverseWordsInAString(unittest.TestCase):
    def test_reverse_words_in_a_string(self):
        solution = Solution()
        actual_list = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ',
                       'i', 's', ' ', 'b', 'l', 'u', 'e']
        expected_list = ['b', 'l', 'u', 'e', ' ', 'i', 's',
                         ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        solution.reverseWords(actual_list)

        self.assertListEqual(expected_list, actual_list)
