import unittest
from leetcode.algorithms.p0557_reverse_words_in_a_string_iii import Solution


class TestReverseWordsInAString(unittest.TestCase):
    def test_reverse_words_in_a_string(self):
        solution = Solution()

        self.assertEqual(
            's\'teL ekat edoCteeL tsetnoc',
            solution.reverseWords('Let\'s take LeetCode contest'))
