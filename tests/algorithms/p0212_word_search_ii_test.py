import unittest
from leetcode.algorithms.p0212_word_search_ii import Solution


class TestWordSearch(unittest.TestCase):
    def test_word_search(self):
        solution = Solution()
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        words = ['oath', 'pea', 'eat', 'rain']
        expected_lists = ['eat', 'oath']
        actual_lists = sorted(solution.findWords(board, words))

        for i in range(len(expected_lists)):
            self.assertEqual(expected_lists[i], actual_lists[i])
