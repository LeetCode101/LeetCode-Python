import unittest
from leetcode.algorithms.p1255_maximum_score_words_formed_by_letters \
    import Solution


class TestMaximumScoreWordsFormedByLetters(unittest.TestCase):
    def test_maximum_score_words_formed_by_letters(self):
        solution = Solution()

        self.assertEqual(23, solution.maxScoreWords(
            ['dog', 'cat', 'dad', 'good'],
            ['a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'],
            [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(27, solution.maxScoreWords(
            ['xxxz', 'ax', 'bx', 'cx'], ['z', 'a', 'b', 'c', 'x', 'x', 'x'],
            [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))
        self.assertEqual(0, solution.maxScoreWords(
            ['leetcode'], ['l', 'e', 't', 'c', 'o', 'd'],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,
             0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
