import unittest
from leetcode.algorithms.p0079_word_search import Solution


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        solution = Solution()

        self.assertTrue(solution.exist(
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']], 'SEE'))
        self.assertFalse(solution.exist(
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']], 'ABCB'))
        self.assertTrue(solution.exist(
            [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']], 'ABCCED'))
