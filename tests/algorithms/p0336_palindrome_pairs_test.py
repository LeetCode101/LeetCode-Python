import unittest
from leetcode.algorithms.p0336_palindrome_pairs import Solution


class TestPalindromePairs(unittest.TestCase):
    def test_palindrome_pairs(self):
        solution = Solution()

        self.assertListEqual([], solution.palindromePairs([]))
        self.assertListEqual(
            sorted([[0, 1], [1, 0], [3, 2], [2, 4]]),
            sorted(solution.palindromePairs(
                ['abcd', 'dcba', 'lls', 's', 'sssll'])))
        self.assertListEqual(
            sorted([[0, 1], [1, 0]]),
            sorted(solution.palindromePairs(['bat', 'tab', 'cat'])))
        self.assertListEqual(
            [[0, 1], [1, 0]],
            sorted(solution.palindromePairs(['a', ''])))
