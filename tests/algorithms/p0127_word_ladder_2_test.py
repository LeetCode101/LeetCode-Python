import unittest
from leetcode.algorithms.p0127_word_ladder_2 import Solution


class TestWordLadder(unittest.TestCase):
    def test_word_ladder(self):
        solution = Solution()

        self.assertEqual(4, solution.ladderLength(
            'lost', 'miss', ['most', 'mist', 'miss', 'lost', 'fist', 'fish']))
        self.assertEqual(5, solution.ladderLength(
            'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
        self.assertEqual(0, solution.ladderLength('a', 'b', []))
