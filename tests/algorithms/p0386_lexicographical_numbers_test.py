import unittest
from leetcode.algorithms.p0386_lexicographical_numbers import Solution


class TestLexicographicalNumbers(unittest.TestCase):
    def test_lexicographical_numbers(self):
        solution = Solution()

        self.assertListEqual([1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
                             solution.lexicalOrder(13))
