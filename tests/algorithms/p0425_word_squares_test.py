import unittest
from leetcode.algorithms.p0425_word_squares import Solution


class TestWordSquares(unittest.TestCase):
    def test_word_squares(self):
        solution = Solution()

        self.assertListEqual([], solution.wordSquares([]))
        self.assertListEqual(
            sorted([['ball', 'area', 'lead', 'lady'],
                    ['wall', 'area', 'lead', 'lady']]),
            sorted(solution.wordSquares(
                ['area', 'lead', 'wall', 'lady', 'ball'])))
        self.assertListEqual(
            sorted([['baba', 'abat', 'baba', 'atal'],
                    ['baba', 'abat', 'baba', 'atan']]),
            sorted(solution.wordSquares(['abat', 'baba', 'atan', 'atal'])))
