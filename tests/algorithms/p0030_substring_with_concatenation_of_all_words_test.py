import unittest
from leetcode.algorithms.p0030_substring_with_concatenation_of_all_words \
    import Solution


class TestSubstringWithConcatenationOfAllWords(unittest.TestCase):
    def test_substring_with_concatenation_of_all_words(self):
        solution = Solution()

        self.assertListEqual([], solution.findSubstring('abc', ['foo']))
        self.assertListEqual([], solution.findSubstring(
            'foofoo', ['foo', 'bar']))
        self.assertListEqual([], solution.findSubstring(
            'wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']))
        self.assertListEqual([0, 9], solution.findSubstring(
            'barfoothefoobarman', ['foo', 'bar']))
