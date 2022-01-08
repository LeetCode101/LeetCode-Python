import unittest
from leetcode.algorithms.p0126_word_ladder_ii_1 import Solution


class TestWordLadder(unittest.TestCase):
    def test_word_ladder(self):
        solution = Solution()

        self.assertListEqual(
            sorted([['hit', 'hot', 'dot', 'dog', 'cog'],
                    ['hit', 'hot', 'lot', 'log', 'cog']]),
            sorted(solution.findLadders(
                'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])))
        self.assertListEqual([], solution.findLadders(
            'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
