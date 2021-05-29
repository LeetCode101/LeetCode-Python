import unittest
from leetcode.algorithms.p0648_replace_words import Solution


class TestReplaceWords(unittest.TestCase):
    def test_replace_words(self):
        solution = Solution()

        self.assertEqual('the cat was rat by the bat', solution.replaceWords(
            ['cat', 'bat', 'rat'], 'the cattle was rattled by the battery'))
