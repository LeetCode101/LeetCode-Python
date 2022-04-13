import unittest
from leetcode.algorithms.p0784_letter_case_permutation import Solution


class TestLetterCasePermutation(unittest.TestCase):
    def test_letter_case_permutation(self):
        solution = Solution()

        self.assertListEqual(
            sorted(['a1b2', 'a1B2', 'A1b2', 'A1B2']),
            sorted(solution.letterCasePermutation('a1b2'))
        )
        self.assertListEqual(
            sorted(['c', 'C']),
            sorted(solution.letterCasePermutation('C')))
