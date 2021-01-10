import unittest
from leetcode.algorithms.p0267_palindrome_permutation_ii import Solution


class TestPalindromePermutationII(unittest.TestCase):
    def test_palindrome_permutation(self):
        solution = Solution()

        self.assertListEqual([], solution.generatePalindromes('ab'))
        self.assertListEqual(['a'], solution.generatePalindromes('a'))
        self.assertListEqual(['abba', 'baab'],
                             sorted(solution.generatePalindromes('aabb')))
